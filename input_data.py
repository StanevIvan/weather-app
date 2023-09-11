# Make class which collects weather data for any city from user input.
# the class should have a method which returns weather data for the city from the API.
# API key is this: 13598b4424ab2b53a191c2462b53f756. It is from https://openweathermap.org/api

import requests

class Weather:
    def __init__(self, city):
        self.city = city
        self.api_key = "13598b4424ab2b53a191c2462b53f756" # Place your API key here.
        self.url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}"

    def get_weather(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            return "Error"


city = input("Enter city: ")
weather = Weather(city)
print(weather.get_weather())
