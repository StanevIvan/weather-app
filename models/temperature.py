from data.forecast import WeatherData


class Temperature(WeatherData):
    def get_temperature(self):
        temperature = round(float(self.weather_data["main"]["temp"]) - 273.15, 1)
        return f"Temperature: {temperature}°C"
