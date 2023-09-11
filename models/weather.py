from data.forecast import WeatherData


class GetWeather(WeatherData):
    def get_weather(self):
        weather = self.weather_data["weather"][0]["main"]
        return weather
