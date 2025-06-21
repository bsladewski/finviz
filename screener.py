"""A stock market screener that scrapes data from FinViz."""
import argparse
import pandas as pd
import requests

from bs4 import BeautifulSoup
from config import Config
from enum import Enum
from io import StringIO
from pandas import DataFrame
from screener_filters import Filters
from screener_sort_options import SortOptions
from utils import Bcolors, text_to_pascal, pascal_to_snake


class View(str, Enum):
    """
    Relates to a specific tab within the FinViz Screener.
    """
    OVERVIEW='111'
    VALUATION='121'
    FINANCIAL='161'
    OWNERSHIP='131'
    PERFORMANCE='141'
    TECHNICAL='171'
    ETF='181'
    ETF_PERF='191'


class Screener:
    """
    Extracts data from the FinViz Screener site.
    """

    @classmethod
    def _format_sort_option(cls, sort: str) -> str:
        return '-' + sort.replace('_desc', '') if sort.endswith('_desc') else sort

    @classmethod
    def _get_table(cls, filter: Filters | None=None, view: View=View.OVERVIEW, sort: str=None, offset: int=None) -> DataFrame:
        # fetch data from FinViz Screener
        params = filter.get_params() if filter is not None else {}
        params.update({'v': view})
        if sort:
            params.update({'o': cls._format_sort_option(sort)})
        if offset:
            params.update({'r': offset+1}) # add 1 as finviz is 1-indexed but usage for this tool will be 0-indexed
        response = requests.get(Config.SCREENER_BASE_URI, params=params, headers=Config.SCREENER_HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        table_soup = soup.find('table', class_='screener_table')
        table_html = StringIO(str(table_soup))
        table = pd.read_html(table_html)

        def _raise_parse_error(error_message: str):
            raise ValueError(f'Failed to parse table data: {error_message}')

        # we expect a single data frame when scraping data, if we did not get a single data frame,
        # raise an appropriate error message
        if not table:
            _raise_parse_error('no table data found, expected 1!')
        elif len(table) > 1:
            _raise_parse_error('found more than one data frame, expected 1!')

        return table[0]

    @classmethod
    def get(cls, filter: Filters | None=None, view: View=View.OVERVIEW, sort: str=None, offset: int=0) -> DataFrame:
        """Scrapes the specified data from FinViz."""
        return cls._get_table(filter, view, sort, offset)


def _list_filters():
    """Prints all available filters."""
    filter_ids = Filters.get_filter_ids()
    for filter_id in filter_ids:
        print(f'{Bcolors.HEADER}{pascal_to_snake(filter_id)}{Bcolors.ENDC}: {getattr(Filters, filter_id).__doc__.replace('<br>', '').strip()}')


def _list_filter_values(filter: str):
    """Prints all available values for a given filter."""
    try:
        filter_class = getattr(Filters, text_to_pascal(filter))
    except AttributeError:
        print(f'{Bcolors.FAIL}Filter "{filter}" not found. Use `python screener.py -lf` or `python screener.py --list_filters` to see available filters.{Bcolors.ENDC}')
        return
    for value in filter_class.__members__.keys():
        print(f'{Bcolors.HEADER}{value.lower()}{Bcolors.ENDC}')


def _list_views():
    """Prints all available views."""
    for view in View.__members__.keys():
        print(f'{Bcolors.HEADER}{view.lower()}{Bcolors.ENDC}')


def _list_sort_options(view_string: str):
    """Prints all sort options for a given view."""
    for option in getattr(SortOptions, text_to_pascal(view_string)).__members__.keys():
        print(f'{Bcolors.HEADER}{option.lower()}{Bcolors.ENDC}')


def _run_screener(filter_strings: list[str], view_string: str, sort_string: str, offset: int):
    """Prints the screening data for the supplied filters and view."""
    if not view_string:
        view = View.OVERVIEW.name
    else:
        try:
            # read the view from user arguments
            view = getattr(View, f'{view_string.upper()}')
        except AttributeError:
            print(f'{Bcolors.FAIL}View "{view_string}" not found. Use `python screener.py -lv` or `python screener.py --list-views` to see available views.{Bcolors.ENDC}')
            return

    filters = Filters()
    for filter_string in filter_strings or []:
        # read filters from user arguments
        filter_string_parts = filter_string.split(':')
        if len(filter_string_parts) != 2:
            # filters are specified in two parts, filter id and filter value
            print(f'{Bcolors.FAIL}Filter "{filter_string}" is formatted incorrectly, the correct format is "<filter_id>:<filter_value>."{Bcolors.ENDC}')
            return
        try:
            # each filter should have an automatically generally "setter" function created by screener_filter_builder.py
            filter_func = getattr(filters, f'filter_{filter_string_parts[0]}')
        except AttributeError:
            print(f'{Bcolors.FAIL}Filter "{filter_string_parts[0]}" not found. Use `python screener.py -lf` or `python screener.py --list_filters` to see available filters.{Bcolors.ENDC}')
            return
        # apply the filter
        try:
            filter = getattr(Filters, f'{text_to_pascal(filter_string_parts[0])}')
            filter_func(getattr(filter, f'{filter_string_parts[1].upper()}'))
        except AttributeError:
            print(f'{Bcolors.FAIL}Filter value "{filter_string_parts[1]}" not found for filter "{filter_string_parts[0]}".Use `python screener.py -lfv` or `python screener.py --list_filter_values` to see available filters values.{Bcolors.ENDC}')
            return
    # print the resulting table from the supplied filters and view
    try:
        data = Screener.get(filters, view, sort_string, offset)
    except ValueError as e:
        print(f'{Bcolors.FAIL}Failed to fetch data: {e}{Bcolors.ENDC}')
        return

    print(data)


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser(
        prog='FinViz Screener',
        description='Scrapes data from the FinViz Screener site.',
        usage='python screener.py -v financial -f industry:asset_management'
    )

    # informational flags
    argument_parser.add_argument('-lf', '--list-filters', action='store_true', help='lists all available filters')
    argument_parser.add_argument('-lfv', '--list-filter-values', type=str, help='lists all available values for a specific filter')
    argument_parser.add_argument('-lv', '--list-views', action='store_true', help='lists all available views')
    argument_parser.add_argument('-lso', '--list-sort-options')

    # functional flags
    argument_parser.add_argument('-f', '--filters', nargs='*', help='applies filters to the result set')
    argument_parser.add_argument('-v', '--view', type=str, help='the tab within FinViz to pull data from')
    argument_parser.add_argument('-s', '--sort', type=str, help='specifies how result data should be sorted')
    argument_parser.add_argument('-o', '--offset', type=int, help='how many records to skip in the result data')
    args = argument_parser.parse_args()

    # handle -lf/--list-filters argument
    if args.list_filters:
        _list_filters()
        quit()

    # handle -lfv/--list-filter-values argument
    if args.list_filter_values:
        _list_filter_values(args.list_filter_values)
        quit()

    # handle -lv/--list-views argument
    if args.list_views:
        _list_views()
        quit()

    # handle -lso/--list-sort-options argument
    if args.list_sort_options:
        _list_sort_options(args.list_sort_options)
        quit()

    # handle command execution
    _run_screener(args.filters, args.view, args.sort, args.offset)
