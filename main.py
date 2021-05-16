import os
import Weather
from twilio.rest import Client


account_sid ='ACedbc739bf228cb311f4147a98a0cfe77'
auth_token = '82f860489d8701d063f20e9f5dd711b5'

weatherlist = Weather.CurrentWeather("Chennai")

client = Client(account_sid, auth_token)

message = client.api.account.messages.create(
    to="+917904900334",
    from_="+15186926126",
    body="\n\n\n\nHello Boss! \nToday's Weather Report for Chennai: \n\nCurrent Temperature - {0}\nMaxiumum Temperature - {1}\nMinimum Temperature - {2}\nForecast - {3}".format(weatherlist[0],weatherlist[1],weatherlist[2],weatherlist[3]))

print(message.account_sid)
