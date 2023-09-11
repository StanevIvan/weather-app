from data.forecast import WeatherData


class Humidity(WeatherData):

    def get_humidity(self):
        humidity = self.weather_data["main"]["humidity"]
        return humidity
