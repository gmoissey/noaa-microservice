from dataclasses import dataclass
from typing import List

@dataclass
class ForecastPeriod:
    name: str
    temperature: int
    temperature_unit: str
    short_forecast: str

@dataclass
class WeatherForecast:
    location: str
    forecast: List[ForecastPeriod]

def to_weather_forecast(data: dict) -> WeatherForecast:
    return WeatherForecast(
        location=data['location'],
        forecast=[ForecastPeriod(
            name=p['name'],
            temperature=p['temperature'],
            temperature_unit=p['temperatureUnit'],
            short_forecast=p['shortForecast']
        ) for p in data['forecast']]
    )