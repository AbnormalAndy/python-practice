from datetime import date, timedelta
import config
import requests


API_KEY_STOCK = config.API_KEY_STOCK
URL_STOCK_API = 'https://www.alphavantage.co/query'


API_KEY_NEWS = config.API_KEY_NEWS
URL_NEWS_API = 'https://newsapi.org/v2/everything'


STOCK = "AAPL"
COMPANY_NAME = "Apple"


today = date.today()
yesterday = date.today() - timedelta(days=1)


params_stock = {
    'apikey': API_KEY_STOCK,
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
}


params_news = {
    'q': COMPANY_NAME,
    'from': today,
    'to': yesterday,
    'language': 'en',
    'sortBy': 'popularity',
    'apiKey': API_KEY_NEWS,
}


# Monday 0, Tuesday 1, Wednesday 2, Thursday 3, Friday 4, Saturday 5, Sunday 6
match today.weekday():
    # Monday: Previous stock day is minus 3. Previous previous stock day is minus 4.
    case 0:
        previous_stock_day = date.today() - timedelta(days=3)
        previous_previous_stock_day = date.today() - timedelta(days=4)
        print('Today is Monday.')
    # Tuesday: Previous stock day is minus 1. Previous previous stock day is minus 4.
    case 1:
        previous_stock_day = date.today() - timedelta(days=1)
        previous_previous_stock_day = date.today() - timedelta(days=4)
        print('Today is Tuesday.')
    # Saturday: Previous stock day is minus 1. Previous previous stock day is minus 2.
    case 5:
        previous_stock_day = date.today() - timedelta(days=1)
        previous_previous_stock_day = date.today() - timedelta(days=2)
        print('Today is Saturday.')
    # Sunday: Previous stock day is minus 2. Previous previous stock day is minus 3.
    case 6:
        previous_stock_day = date.today() - timedelta(days=2)
        previous_previous_stock_day = date.today() - timedelta(days=3)
        print('Today is Sunday.')
    # Other Days: Previous stock day is minus 1. Previous previous stock day is minus 2.
    case _:
        previous_stock_day = date.today() - timedelta(days=1)
        previous_previous_stock_day = date.today() - timedelta(days=2)
        print('Today is a day not to worry.')


response_stock = requests.get(url=URL_STOCK_API, params=params_stock)
response_stock.raise_for_status()
data_stock = response_stock.json()


# Retrieves the previous STOCK day's open and close numbers.
previous_open = data_stock['Time Series (Daily)'][str(previous_stock_day)]['1. open']
previous_close = data_stock['Time Series (Daily)'][str(previous_stock_day)]['4. close']


# Retrieves the previous previous STOCK day's open and close numbers.
previous_previous_open = data_stock['Time Series (Daily)'][str(previous_previous_stock_day)]['1. open']
previous_previous_close = data_stock['Time Series (Daily)'][str(previous_previous_stock_day)]['4. close']


# Calculates the change in stock price from preivous previous stock day to previous stock day.
percentage_of_change = (float(previous_close) - float(previous_previous_close)) / float(previous_previous_close) * 100


# Used to DEBUG
#percentage_of_change = (200 - 300) / 300 * 100


# Used to DEBUG
#print(f'This is the previous stock day close: {previous_close}')
#print(f'This is the previous previous stock day close: {previous_previous_close}')
#print(f'This is the percentage of change: {percentage_of_change}')


# Retrieves relevant news to company if stock change is greater than 10% or less than 10%.
if percentage_of_change >= 10 or percentage_of_change <= -10:
    response_news = requests.get(url=URL_NEWS_API, params=params_news)
    response_news.raise_for_status()
    data_news = response_news.json()


    article_one_headline = data_news['articles'][0]['title']
    article_one_brief =data_news['articles'][0]['description']


    article_two_headline = data_news['articles'][1]['title']
    article_two_brief = data_news['articles'][1]['description']


    article_three_headline = data_news['articles'][2]['title']
    article_three_brief = data_news['articles'][2]['description']


    news_to_print = f"""
    AAPL: {percentage_of_change:.2f}%
    Headline One: {article_one_headline}
    Brief One: {article_one_brief}

    Headline Two: {article_two_headline}
    Brief Two: {article_two_brief}

    Headline Three: {article_three_headline}
    Brief Three: {article_three_brief}
    """

    print(news_to_print)


else:
    print(f"No major changes in {COMPANY_NAME}'s stock.")


