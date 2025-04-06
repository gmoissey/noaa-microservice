from flask import Blueprint, jsonify
from app.services.weather import get_weather_forecast_by_location
from http import HTTPStatus

bp = Blueprint('weather-api', __name__, url_prefix='/weather-api')

@bp.route('/location/<location>', methods=['GET'])
def get_weather(location: str):
    try:
        forecast = get_weather_forecast_by_location(location)
        return jsonify(forecast), HTTPStatus.OK
    except ValueError as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

@bp.route('/requests', methods=['GET'])
def get_requests():
    return jsonify({'requests': 'success'}), HTTPStatus.OK