import requests
from typing import Dict, Any

WEATHER_API_BASE = "https://api.weather.gov"
HEADERS = {"User-Agent": "WeatherAPI/1.0 (glebmois@gmail.com)"}

class NOAAWeatherClient:
    @staticmethod
    def get_grid_from_lat_lon(lat: float, lon: float) -> Dict[str, Any]:
        url = f"{WEATHER_API_BASE}/points/{lat},{lon}"
        response = requests.get(url, headers=HEADERS, timeout=5)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_forecast_from_grid(grid_data: Dict[str, Any]) -> Dict[str, Any]:
        forecast_url = grid_data['properties']['forecast']
        response = requests.get(forecast_url, headers=HEADERS, timeout=5)
        response.raise_for_status()
        return response.json()