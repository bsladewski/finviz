# finviz

This repository contains tools for interacting with the finviz site using python.

## Screener

The screener provides functions for fetching data from the screener page of the finviz site. The
screener can be imported and used in applications as a source of data or the screener can be run as
a CLI tool.

### Usage

Usage as a python package:

```python
from finviz.screener_filters import Filters
from finviz.screener_sort_options import SortOptions
from finviz.screener import View, Screener

# setting up filters
filters = Filters()
filters.filter_industry(Filters.Industry.FOOD_DISTRIBUTION)
filters.filter_country(Filters.Country.USA)

# basic usage
screener = Screener()
screener.get(filters)

# selecting a view
screener.get(filters, view=View.TECHNICAL)

# offsetting data (ex. for pagination)
screener.get(filters, offset=20)

# sorting data
screener.get(filters, sort=SortOptions.Overview.PRICE)
```

Usage as a CLI:

```bash
python screener.py -h # print help text

# list data available to the screener tool
python screener.py -lf            # filters
python screener.py -lfv industry  # values for a given filter
python screener.py -lv            # views
python screener.py -lso overview  # sorting options for a given view

# fetch data from the finviz screener page
python screener.py -v valuation                                          # unfiltered from a specific tab
python screener.py -f industry:biotechnology                             # singe filter
python screener.py -f industry:biotechnology country:canada              # multiple filters
python screener.py -v valuation -f industry:biotechnology country:canada # filtered from a specific tab

# other options
python screener.py -o 20           # skip the first 20 records of results
python screener.py -s company      # sort by company column ascending
python screener.py -s company_desc # sort by company column descending

# rebuild/update screener filters
python screener_filters_builder.py

# rebuild/update sort options
python screener_sort_options_builder.py
```
