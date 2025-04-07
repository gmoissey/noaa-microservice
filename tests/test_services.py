import pytest
from app.services.weather import get_weather_forecast, get_weather_forecast_by_location

def test_get_weather_forecast(mock_noaa_weather):
    result = get_weather_forecast(40.0, -96.0)
    assert result['location'] == 'TestCity, TS'
    assert result['forecast'][0]['temperature'] == 70

def test_get_weather_forecast_by_location_valid(mock_noaa_weather):
    result = get_weather_forecast_by_location('40.777422,-96.676480')
    assert result['location'] == 'TestCity, TS'
    assert len(result['forecast']) == 1

def test_get_weather_forecast_by_location_invalid():
    with pytest.raises(ValueError, match='Invalid location format.*'):
        get_weather_forecast_by_location('invalid')

    with pytest.raises(ValueError, match='Latitude must be -90 to 90.*'):
        get_weather_forecast_by_location('91.0,-96.0')

    with pytest.raises(ValueError, match='Invalid location format.*'):
        get_weather_forecast_by_location('abc,def')
