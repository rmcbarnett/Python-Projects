# This script checks the price changes for Tesla for the two preceeding days and informs the user of possible reasons for the changes.
# It uses two end points to achieve this
# This is done by sending the user a text with the most recent news updates.
# All sensitive fields have been removed



import requests
from twilio.rest import Client
import datetime as dt

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = ''
TESLA_API_KEY = '' 
CLOSING_TIME= '20:00:00'
account_sid = ''
auth_token=''


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters= {
    'function': 'TIME_SERIES_INTRADAY',
    'symbol':STOCK_NAME,
    'interval':'60min',
    'apikey': STOCK_API_KEY

}

news_parameters = {
    'apikey':TESLA_API_KEY,
    'q':COMPANY_NAME,
    'from':'2022-05-24'
}
## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 1% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]


response = requests.get(STOCK_ENDPOINT,params=parameters)
response.raise_for_status()
stock_data = response.json()
stock_data = stock_data['Time Series (60min)']
print(stock_data)
print(stock_data['2022-05-23 20:00:00'])

today = dt.datetime.now()
yesterday = dt.datetime.today() - dt.timedelta(days=1)

# checking to see if the weekday is a business day
while yesterday.weekday() > 4:
    yesterday = yesterday - dt.timedelta(days=1)

day_before_yesterday = yesterday - dt.timedelta(days=1)
while day_before_yesterday.weekday() > 4:
    day_before_yesterday = day_before_yesterday - dt.timedelta(days=1)
print('DDD')

year = yesterday.year
month = yesterday.month

# Need to format the day & month  to start with 0 if its less than 10
if month < 10: month = f'0{month}'
day = yesterday.day
if day< 10: month = f'0{day}'
yesterday_closing = f'{yesterday.year}-{month}-{day} {CLOSING_TIME}'
print(yesterday_closing)

#TODO 2. - Get the day before yesterday's closing stock price
year = day_before_yesterday.year
month = day_before_yesterday.month
if month < 10: month = f'0{month}'
day = day_before_yesterday.day
if day< 10: month = f'0{day}'
day_before_yesterday_closing = f'{year}-{month}-{day} {CLOSING_TIME}'
print(day_before_yesterday_closing)

yesterday_closing_price = float(stock_data[yesterday_closing]['4. close'])
day_before_yesterday_closing_price = float(stock_data[day_before_yesterday_closing]['4. close'])



#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.


price_difference = abs(yesterday_closing_price - day_before_yesterday_closing_price )
print(price_difference)




#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

price_percentage = round((price_difference/yesterday_closing_price) *100,2)
print(price_percentage)






#TODO 5. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if price_percentage> 1 :
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    news_data = response.json()




#TODO 6. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    news_data_slice= news_data['articles'][:3]
    print(news_data_slice)

#TODO 7. - Create a new list of the first 3 article's headline and description using list comprehension.

    formatted_news_list = [f'TSLA: {price_percentage} %\n Headline: {x["title"]}\n Brief: {x["description"]}' for x in news_data_slice]

    print(formatted_news_list)

#TODO 8. - Send first article as a  message via Twilio.
    client = Client(account_sid, auth_token)
    message = client.api.account.messages.create(
        to="",
        from_="",
        body=formatted_news_list[0])

print(message.status)




