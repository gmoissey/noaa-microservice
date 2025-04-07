import pytest
from http import HTTPStatus

def test_get_weather_success(client, mock_noaa_weather):
    response = client.get('/weather-api/location/40.777422,-96.676480')
    assert response.status_code == HTTPStatus.OK
    data = response.get_json()
    assert data['location'] == 'TestCity, TS'
    assert len(data['forecast']) == 1
    
    db = client.application.config['TEST_DB']
    request_log = db.requests.find_one({'location': '40.777422,-96.676480'})
    assert request_log['status'] == HTTPStatus.OK
    assert 'response' in request_log
    assert request_log['response']['location'] == 'TestCity, TS'

def test_get_weather_invalid(client):
    response = client.get('/weather-api/location/invalid')
    assert response.status_code == HTTPStatus.BAD_REQUEST
    data = response.get_json()
    assert 'error' in data
    
    db = client.application.config['TEST_DB']
    request_log = db.requests.find_one({'location': 'invalid'})
    assert request_log['status'] == HTTPStatus.BAD_REQUEST
    assert 'error' in request_log

def test_get_requests(client, mock_noaa_weather):
    # Make some requests to populate the DB
    client.get('/weather-api/location/39.7392,-104.9904')
    client.get('/weather-api/location/40.777422,-96.676481')
    
    response = client.get('/weather-api/requests?limit=1')
    assert response.status_code == HTTPStatus.OK
    data = response.get_json()
    assert len(data['requests']) == 1
    
    # This expects the first request is returned
    assert data['requests'][0]['location'] == '39.7392,-104.9904'
    assert 'timestamp' in data['requests'][0]

def test_get_requests_invalid_limit(client):
    response = client.get('/weather-api/requests?limit=0')
    assert response.status_code == HTTPStatus.BAD_REQUEST
    data = response.get_json()
    assert 'error' in data
