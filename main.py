import requests
from twilio.rest import  Client

Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "71f9af2ce6c1d9720531780249fd41fe"
account_sid = "AC9bdf2228acb46552d6ae0b5f89d11e91"
auth_token = "1744363a6d388ae867756b112e9d9746"
#client = Client(account_sid, auth_token)




weather_params = {
    "lat":22.574535,
    "lon":88.433418,
    "appid":api_key,
    "cnt": 4,

}
response = requests.get(Endpoint,params=weather_params)
response.raise_for_status()
weather_data = response.json()
#print(weather_data["list"][0]["weather"][0]["id"])
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code)< 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="bring umbrella",
            from_='+14698046171',
            to='+917044376943'
        )
    else:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="its hot as hell , stay in door and drink water please",
            from_='+14698046171',
            to='+917044376943'
        )
        print(message.status)