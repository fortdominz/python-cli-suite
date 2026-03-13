import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

TWILIO_SID = "YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"

AV_API_KEY = "YOUR_ALPHAVANTAGE_API_KEY"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_price_parameters = {
    "apikey": AV_API_KEY,
    "symbol": STOCK_NAME,
    "function": "TIME_SERIES_DAILY",
    "outputsize": 0,
}
news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }

stock_price_url = "https://www.alphavantage.co/query"
news_url = "https://newsapi.org/v2/everything"


stock_price_response = requests.get(url= stock_price_url, params=stock_price_parameters)
stock_price_response.raise_for_status()
stock_price_data = stock_price_response.json()


closing_prices = []
for day, data_for_day in stock_price_data['Time Series (Daily)'].items():
    close_price = data_for_day["4. close"]
    closing_prices.append((day, close_price))

yesterday_data = closing_prices[0]
yesterday_closing_price = yesterday_data[1]

day_before_yesterday_data = closing_prices[1]
day_before_yesterday_closing_price = day_before_yesterday_data[1]

positive_difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
green_or_red = None
if positive_difference > 0:
    green_or_red = "▲"
else:
    green_or_red = "🔻"

percentage_difference = round((positive_difference / float(yesterday_closing_price)) * 100)

if abs(percentage_difference) > 3:
    news_response = requests.get(url=news_url, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()

    full_data = []
    for article in news_data["articles"]:
        full_data.append(article)

    top_3 = full_data[:3]
    formatted_news_article = [(f"{STOCK_NAME}: {green_or_red}{percentage_difference}%"
                               f"\nHeadlines: {section["title"]}."
                               f"\nBrief: {section["description"]}.")
                              for section in top_3]


    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for each_news_article in formatted_news_article:
        message = client.messages.create(
            body= each_news_article,
            from_= "AUTOMATED_NUMBER",
            to= "YOUR_NUMBER",
        )

