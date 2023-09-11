from data.forecast import WeatherData


class FeelsLikeTemperature(WeatherData):

    def feels_like(self):
        feels_like = round(float(self.weather_data["main"]["feels_like"]) - 273.15, 1)
        return f"Feels like: {feels_like}°C"
