import re
from typing import Dict, Any
from app.clients.noaa_weather import NOAAWeatherClient

def get_weather_forecast(lat: float, lon: float) -> Dict[str, Any]:
    grid_data = NOAAWeatherClient.get_grid_from_lat_lon(lat, lon)
    forecast_data = NOAAWeatherClient.get_forecast_from_grid(grid_data)
    periods = forecast_data['properties']['periods']
    return {
        'location': f"{grid_data['properties']['relativeLocation']['properties']['city']}, "
                    f"{grid_data['properties']['relativeLocation']['properties']['state']}",
        'forecast': [
            {
                'name': period['name'],
                'temperature': period['temperature'],
                'temperatureUnit': period['temperatureUnit'],
                'shortForecast': period['shortForecast']
            }
            for period in periods[:3]
        ]
    }

def get_weather_forecast_by_location(location: str) -> Dict[str, Any]:
    # Regex to match lat,lon format (e.g., 40.777422,-96.676480)
    pattern = r'^(-?\d{1,2}\.\d+|-?90\.0+|-?\d{1,2}),(-?\d{1,3}\.\d+|-?180\.0+|-?\d{1,3})$'
    
    if not re.match(pattern, location):
        raise ValueError('Invalid location format. Use <lat>,<lon> (e.g., 40.777422,-96.676480)')
    
    lat_str, lon_str = location.split(',')
    try:
        lat = float(lat_str)
        lon = float(lon_str)
    except ValueError:
        raise ValueError('Latitude and Longitude must be valid numbers')
    
    if not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
        raise ValueError('Latitude must be -90 to 90, Longitude must be -180 to 180')
    
    return get_weather_forecast(lat, lon)