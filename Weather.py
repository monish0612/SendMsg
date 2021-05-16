import requests, json


def CurrentWeather(city):
    baseurl = "https://api.openweathermap.org/data/2.5/weather?q="
    cityname = city
    apikey = "2aa7cc0ebe35958d9083d9e724d084af"

    baseurl = baseurl + cityname + "&appid=" + apikey

    response = requests.get(baseurl)

    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        currenttemp = main["temp"] - 273.15
        mintemp = main["temp_min"] - 273.15
        maxtemp = main["temp_max"] - 273.15
        humidity = main["humidity"]
        report = data["weather"][0]
        skystatus = report["description"]

    return currenttemp,maxtemp,mintemp,skystatus





