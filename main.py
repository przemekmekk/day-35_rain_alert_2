import requests
import smtplib

my_email = "janbrzechwaproba@gmail.com"
password=""
api_key = "5cb5faa3c4c892b3c1b5020b6dd7db84"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# lon : 18.530540,
# "lat" : 54.518890, #
weather_params = {
    "lat" : 11.874477,
    "lon": 75.370369,
    # "lat" : 18.530540,
    # "lon":54.518890,
    "appid" : api_key,
    "exclude": "current, hourly,daily,minutely",
}

def sending_email(text):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="konickiprzemyslaw@gmail.com",
                            msg=f"Subject:Alert pogodowy!\n{text}")
# MY_LAT = 54.518890 # Your latitude
# MY_LONG = 18.530540 # Your longitude
#response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?lat=54.518890&lon=18.530540&exclude=hourly,daily&appid=5cb5faa3c4c892b3c1b5020b6dd7db84")
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
# days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# for i in range(0,7):
#     temp = (data["daily"][i]["temp"]["day"])-273
#     print(round(temp),days[i])
# print(data)
point=False
for i in range(7,19):
    weather = data["hourly"][i]["weather"][0]["id"]
    if weather < 700:
        point=True
        # print(weather)
if point:
    print("weź parasol bo bedzie padać")
    # sending_email(text="Weź parasol bo będzie padać :) ")
else:
    print("nie musisz brać parasola")
    # sending_email(text="Nie bedzie dzis padac, nie musisz brac parasola!")

