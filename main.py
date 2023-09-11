from models.weather import GetWeather
from models.temperature import Temperature
from models.feels_like_temperature import FeelsLikeTemperature
from models.humidity import Humidity


class WeatherReport(GetWeather, Temperature, FeelsLikeTemperature, Humidity):
    def __init__(self, city):
        super().__init__(city, apikey="13598b4424ab2b53a191c2462b53f756")
        self.city = city

    def weather_report(self):
        weather = self.get_weather()
        temperature = self.get_temperature()
        feels_like = self.feels_like()
        humidity = self.get_humidity()
        return f"City: {self.city}\nWeather: {weather}\n{temperature}\n{feels_like}\nHumidity: {humidity}%"


def main():
    city = input("Enter the city name: ")
    weather_report = WeatherReport(city)
    print(weather_report.weather_report())


if __name__ == "__main__":
    main()
