class Config:
    """
    Base configuration for scraping FinViz.
    """
    SCREENER_BASE_URI = 'https://finviz.com/screener.ashx'
    SCREENER_HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
