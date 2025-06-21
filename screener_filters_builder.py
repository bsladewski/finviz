"""Utilities for building FinViz filters."""
import re
import requests

from bs4 import BeautifulSoup
from config import Config
from typing import Tuple
from utils import text_to_pascal, text_to_screaming_snake, pascal_to_snake


class ScreenerFiltersBuilder:
    """
    A utility class for generating a python file that can be used to build FinViz Screener filters.

    This class will scrape the FinViz Screener site and parse all freely available filters and all
    of the options available for each filter.
    """

    @classmethod
    def _parse_row(cls, row) -> Tuple[dict, dict]:
        column = 0
        current_label = None
        filters = {}
        filter_descriptions = {}
        seen_filters = set()

        # iterate over columns of the row to extract filter data
        for data in row.find_all('td', recursive=False):
            if column % 2 == 0:
                # if the row index is even, extract the label for the filter
                span = data.find('span')
                if span is None:
                    break

                current_label = span.text
                day_prefix_match = re.match(r'^\d+.?Day', current_label)
                if day_prefix_match:
                    # if we have a filter like "20-Day Simple Moving Average", format the id like "SimpleMovingAverage20Day"
                    current_label = text_to_pascal(current_label[day_prefix_match.end():]) + day_prefix_match.group(0)
                    current_label = re.sub(r'[^0-9a-zA-Z]+', '', current_label)
                else:
                    # convert the label text to PascalCase
                    current_label = text_to_pascal(current_label)

                # deduplicate filters
                if current_label in seen_filters:
                    continue
                else:
                    seen_filters.add(current_label)

                # parse label tooltip
                tooltip_match = re.match(r"(.+?)(<td class='tooltip_tab'>)(.+?)(</td>)(.+?)", span['data-boxover'])
                if tooltip_match:
                    # if we found a tooltip for this label, add it to the filter descriptions map
                    filter_descriptions[current_label] = tooltip_match.group(3)
                else:
                    # if we did not find a tooltip for this label, add a TODO so it can be manually fixed later
                    filter_descriptions[current_label] = 'TODO: add filter description'
            else:
                # if the row index is odd, extract the options for the filter
                select = data.find('select')
                if select is None:
                    break

                options = []
                seen_option_ids = set()
                seen_value_ids = set()

                # build options for the current filter
                for option in select.find_all('option', recursive=False):
                    if 'disabled' in select:
                        # skip labels that are disabled (they require a paid account)
                        break

                    if not option['value'] or 'Elite only' in option.text:
                        # skip options that are disabled (they require a paid account)
                        continue

                    # add the data required to build the option enum to the list of options for this filter
                    id = text_to_screaming_snake(option.text)
                    value = select['data-filter'] + '_' + option['value']

                    # deduplicate options
                    if id in seen_option_ids or value in seen_value_ids:
                        continue
                    else:
                        seen_option_ids.add(id)
                        seen_value_ids.add(value)

                    options.append({'id': id, 'value': value})

                if len(options) > 0:
                    # if we parsed any options for the current filter, add it to the filter dictionary
                    filters[current_label] = options

            column += 1

        return filters, filter_descriptions

    @classmethod
    def _get_filters(cls) -> Tuple[dict, dict]:
        # fetch the contents of the FinViz Screener filters element
        params = {'v': '111', 'ft': '4'}
        response = requests.get(Config.SCREENER_BASE_URI, params=params, headers=Config.SCREENER_HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        table_soup = soup.find('table', id='filter-table-filters')

        # parse each row of filters
        filters = {}
        filter_descriptions = {}
        for row in table_soup.find_all('tr', recursive=False):
            row_filters, row_descriptions = cls._parse_row(row)
            filters.update(row_filters)
            filter_descriptions.update(row_descriptions)

        return filters, filter_descriptions

    @classmethod
    def _write_filter(cls, output_file, filter_id: str, filter_options: list[dict], filter_description: str):
        # write the enum class definition
        output_file.write(f'    class {filter_id}(str, Enum):\n')
        output_file.write('        """\n')
        output_file.write(f'        {filter_description}\n')
        output_file.write('        """\n')

        # write each enum value
        for option in filter_options:
            output_file.write('        {}=\'{}\'\n'.format(option['id'].upper(), option['value']))

        # define a function to filter by this field
        filter_id_snake = pascal_to_snake(filter_id)
        output_file.write(f'\n    def filter_{filter_id_snake}(self, {filter_id_snake}: {filter_id}):\n')
        output_file.write('        self.filters[\'{}\'] = {}\n\n'.format(filter_id, filter_id_snake))

    @classmethod
    def build_filter_class_file(cls):
        """
        Generates a python file with a class for building FinViz Screener filters.
        """
        filters, filter_descriptions = cls._get_filters()
        with open('screener_filters.py', 'w', encoding='utf-8') as output_file:
            # create imports
            output_file.write('from enum import Enum\n\n')

            # creates top level class definition
            output_file.write('class Filters(object):\n')
            output_file.write('    """\n')
            output_file.write('    Provides filter parameters for interacting with the FinViz Screening site.\n')
            output_file.write('    """\n\n')

            # creates class init function
            output_file.write('    def __init__(self, manual_filters: list[str] | None=None):\n')
            output_file.write('        self.filters = {}\n')
            output_file.write('        self.manual_filters = manual_filters or []\n\n')

            # create enums for all available filters
            for filter_id in filters.keys():
                cls._write_filter(output_file, filter_id, filters[filter_id], filter_descriptions[filter_id])

            # create function to convert filters to FinViz Screener query parameters
            output_file.write('    def get_params(self) -> dict:\n')
            output_file.write('        """\n')
            output_file.write('        Returns filter parameters in the format expected by FinViz.\n')
            output_file.write('        """\n')
            output_file.write('        params = {\'f\': \',\'.join(self.filters.values())}\n')
            output_file.write('        if self.manual_filters:\n')
            output_file.write('            params[\'f\'] += \',\' + \',\'.join(self.manual_filters)\n')
            output_file.write('        return params\n\n')

            # create function to retrieve all filter ids
            output_file.write('    @classmethod\n')
            output_file.write('    def get_filter_ids(cls) -> list[str]:\n')
            output_file.write('        """\n')
            output_file.write('        Returns a list of available filter ids as strings.\n')
            output_file.write('        """\n')
            output_file.write('        return [\n')
            for filter_id in filters.keys():
                output_file.write(f'            \'{filter_id}\',\n')
            output_file.write('        ]\n')


if __name__ == '__main__':
    ScreenerFiltersBuilder.build_filter_class_file()
