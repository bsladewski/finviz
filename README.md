# finviz

This repository contains tools for interacting with the finviz site with python.

## Screener

The screener provides functions for fetching data from the screener page of the finviz site. The
screener can be imported and used in applications as a source of data or the screener can be run as
a CLI tool.

### Usage

Usage as a python package:

```python
from finviz.screener_filters import Filters
from finviz.screener import View, Screener

filters = Filters()
filters.filter_industry(Filters.Industry.FOOD_DISTRIBUTION)
filters.filter_country(Filters.Country.USA)

screener = Screener()
screener.get(filters, View.TECHNICAL)
```

Usage as a CLI:

```bash
# list data available to the screener tool
python screener.py -lf           # filters
python screener.py -lfv industry # values for a given filter
python screener.py -lv           # views

# fetch data from the finviz screener page
python screener.py -v valuation                                          # unfiltered from a specific tab
python screener.py -f industry:biotechnology                             # singe filter
python screener.py -f industry:biotechnology country:canada              # multiple filters
python screener.py -v valuation -f industry:biotechnology country:canada # filtered from a specific tab

# rebuild/update screener filters
python screener_filters_builder.py
```
