import pytest
from app import create_app
from mongomock import MongoClient as MockMongoClient
from flask import g
from typing import Dict, Any

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
        'MONGO_URI': 'mongodb://localhost:27017/test_db'
    })
    
    mongo_client = MockMongoClient()
    db = mongo_client['test_db']

    app.config['TEST_DB'] = db
    
    @app.before_request
    def inject_mock_db():
        g.db = db
    
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def mock_noaa_weather(monkeypatch):
    class MockNOAAWeatherClient:
        @staticmethod
        def get_grid_from_lat_lon(lat: float, lon: float) -> Dict[str, Any]:
            return {
                'properties': {
                    'relativeLocation': {'properties': {'city': 'TestCity', 'state': 'TS'}},
                    'forecast': 'mock_forecast_url'
                }
            }

        @staticmethod
        def get_forecast_from_grid(grid_data: Dict[str, Any]) -> Dict[str, Any]:
            return {
                'properties': {
                    'periods': [
                        {
                            'name': 'Today',
                            'temperature': 70,
                            'temperatureUnit': 'F',
                            'shortForecast': 'Sunny'
                        }
                    ]
                }
            }

    # Patching where weather.py references NOAAWeatherClient
    monkeypatch.setattr('app.services.weather.NOAAWeatherClient', MockNOAAWeatherClient)
