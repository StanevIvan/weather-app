# Make class which collects weather models for any city from user input.
# the class should have a method which returns weather models for the city from the API.
# API key is this: 13598b4424ab2b53a191c2462b53f756. It is from https://openweathermap.org/api
# Use getters and setters for the class.

import requests


class WeatherData:
    def __init__(self, city, apikey):
        self.city = city
        self.apikey = apikey
        self.url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={apikey}"
        self.weather_data = self.get_weather_data()

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        if city.isalpha():
            self.__city = city
        else:
            raise ValueError("City name must contain only letters")

    @property
    def apikey(self):
        return self.__apikey

    @apikey.setter
    def apikey(self, apikey):
        self.__apikey = apikey

    def get_weather_data(self):
        response = requests.get(self.url)
        return response.json()

