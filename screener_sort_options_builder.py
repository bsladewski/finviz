import re
import requests

from bs4 import BeautifulSoup
from config import Config
from utils import text_to_screaming_snake


class ScreenerSortOptionsBuilder:
    """
    A utility class for generating a python file that can be used to build FinViz Screener sort options.

    This class will scrape the FinViz Screener site and parse all available sort options from each view.
    """

    supported_views = {
        'Overview': '111',
        'Valuation': '121',
        'Financial': '161',
        'Ownership': '131',
        'Performance': '141',
        'Technical': '171',
        'Etf': '181',
        'EtfPerformance': '191',
    }

    @classmethod
    def _get_sort_options_for_view(cls, view_id: str) -> list[dict]:
        # fetch the contents of the FinViz Screener filters element
        params = {'v': view_id}
        response = requests.get(Config.SCREENER_BASE_URI, params=params, headers=Config.SCREENER_HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        table_soup = soup.find('table', class_='screener_table')

        # parse table headers
        sort_options = []
        table_headers_soup = table_soup.find('thead', recursive=False).find('tr')
        for header in table_headers_soup.find_all('th', recursive=False):
            # parse header text
            header_text = header.get_text().strip()
            if not header_text or header_text == 'No.':
                continue

            # parse header action
            onclick_text = header['onclick']
            match = re.search(r"[?&]o=([^&']+)", onclick_text)
            if match:
                sort_option_value = match.group(1)
                if sort_option_value.startswith('-'):
                    sort_option_value = sort_option_value[1:]
                sort_options.append({
                    'id': text_to_screaming_snake(header_text),
                    'value': sort_option_value,
                    'name': header_text
                })

        return sort_options

    @classmethod
    def _get_sort_options(cls) -> dict[list[dict]]:
        sort_options_by_view = {}
        for view in cls.supported_views.keys():
            sort_options_by_view[view] = cls._get_sort_options_for_view(cls.supported_views[view])
        return sort_options_by_view

    @classmethod
    def _write_sort_options(cls, output_file, view: str, sort_options: list[dict]):
        # write the enum class definition
        output_file.write(f'    class {view}(str, Enum):\n')

        # write each enum value
        for sort_option in sort_options:
            output_file.write(f'        {sort_option['id'].upper()}=\'{sort_option['value']}\' # {sort_option['name']}\n')
            output_file.write(f'        {sort_option['id'].upper()}_DESC=\'{sort_option['value']}_desc\' # {sort_option['name']} Descending\n')

        output_file.write('\n')

    @classmethod
    def build_sort_options_class_file(cls):
        """
        Generates a python file with a class for building FinViz Screener sort options.
        """
        sort_options_by_view = cls._get_sort_options()
        with open('screener_sort_options.py', 'w', encoding='utf-8') as output_file:
            # create imports
            output_file.write('from enum import Enum\n\n')

            # creates top level class definition
            output_file.write('class SortOptions(object):\n')
            output_file.write('    """\n')
            output_file.write('    Provides sort options for interacting with the FinViz Screening site.\n')
            output_file.write('    """\n\n')

            for view in sort_options_by_view.keys():
                cls._write_sort_options(output_file, view, sort_options_by_view[view])

if __name__ == '__main__':
    ScreenerSortOptionsBuilder.build_sort_options_class_file()
