import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"

LAT = "YOUR_LATITUDE"
LONG = "YOUR_LONGITUDE"

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

rain_incoming = False
for hour_interval in weather_data["list"]:
    weather_info = hour_interval["weather"][0]
    weather_id = weather_info["id"]
    if weather_id < 700:
        rain_incoming = True

if rain_incoming:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(ACCOUNT_SID, AUTH_TOKEN, http_client=proxy_client)

    message = client.messages.create(
        body="It's going to rain today. Bring an Umbrella!",
        from_="AUTOMATED_NUMBER",
        to="YOUR_NUMBER",
    )
    print(message.status)
