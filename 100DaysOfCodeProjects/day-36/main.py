from datetime import date, timedelta
import config
import requests


API_KEY_STOCK = config.API_KEY_STOCK
URL_STOCK_API = 'https://www.alphavantage.co/query'


API_KEY_NEWS = config.API_KEY_NEWS
URL_NEWS_API = 'https://newsapi.org/v2/everything'


STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"


today = date.today()
yesterday = date.today() - timedelta(days=1)


params_stock = {
    'apikey': API_KEY_STOCK,
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
}


params_news = {
    'apiKey': API_KEY_NEWS,
    'searchIn': COMPANY_NAME,
    'from': str(today),
    'to': str(yesterday),
    'language': 'en',
    'sortBy': 'popularity',
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


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response_stock = requests.get(url=URL_STOCK_API, params=params_stock)
response_stock.raise_for_status()
data_stock = response_stock.json()


# Automate previous day - current day minus 1.
# If no close yet, get the day before previous day as well - current day minus 2.
# datetime module?
previous_open = data_stock['Time Series (Daily)'][str(previous_stock_day)]['1. open']
previous_close = data_stock['Time Series (Daily)'][str(previous_stock_day)]['4. close']


previous_previous_open = data_stock['Time Series (Daily)'][str(previous_previous_stock_day)]['1. open']
previous_previous_close = data_stock['Time Series (Daily)'][str(previous_previous_stock_day)]['4. close']


percentage_of_change = (previous_close - previous_previous_close) / previous_close * 100


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
response_news = requests.get(url=URL_NEWS_API, params=params_news)
response_news.raise_for_status()
data_news = response_news.json()


article_one_headline = data_news['articles'][0]['title']
article_one_brief =data_news['articles'][0]['description']


article_two_headline = data_news['articles'][1]['title']
article_two_brief = data_news['articles'][1]['description']


article_three_headline = data_news['articles'][2]['title']
article_three_brief = data_news['articles'][2]['description']


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


print(f"""
AAPL: {percentage_of_change:.2f}%
Headline One: {article_one_headline}
Brief One: {article_one_brief}

Headline Two: {article_two_headline}
Brief Two: {article_two_brief}

Headline Three: {article_three_headline}
Brief Three: {article_three_brief}
""")



#Optional: Format the SMS message like this: 
"""
AAPL: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Apple Inc. (AAPL)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"AAPL: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Apple Inc. (AAPL)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


