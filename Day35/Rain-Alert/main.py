import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OMW_KEY")
account_sid = "AC6a12511824343949ea2cf51ed63870bf"
auth_token = os.environ.get("OMW_TOKEN")

weather_params = {
    "q": "Cleveland, MS, US",
    "cnt": 4,
    "appid": api_key,
    
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for count in weather_data["list"]:
    weather_id = count["weather"][0]["id"]
    
    if weather_id < 701:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)    
    message = client.messages.create(

        body="Grab a ☂️!",
        from_="whatsapp:+14155238886",
        to="whatsapp:+16627194824",

    )
    print(message.body)

else:
    client = Client(account_sid, auth_token)    
    message = client.messages.create(

        body="No rain!",
        from_="whatsapp:+14155238886",
        to="whatsapp:+16627194824",

    )
    print(message.body)


    # if 622 > weather_id > 599:
    #     print("Bundle up.")
    # if weather_id == 800:
    #     print("Clear skies!")
    
    