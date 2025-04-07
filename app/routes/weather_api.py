from flask import Blueprint, jsonify, g, request
from app.services.weather import get_weather_forecast_by_location
from http import HTTPStatus
from datetime import datetime, timezone

bp = Blueprint('weather-api', __name__, url_prefix='/weather-api')

@bp.route('/location/<location>', methods=['GET'])
def get_weather(location: str):
    try:
        forecast = get_weather_forecast_by_location(location)
        
        # Log the request to MongoDB
        g.db.requests.insert_one({
            'location': location,
            'timestamp': datetime.now(timezone.utc),
            'response': forecast,
            'status': HTTPStatus.OK
        })
        
        return jsonify(forecast), HTTPStatus.OK
    except ValueError as e:
        g.db.requests.insert_one({
            'location': location,
            'timestamp': datetime.now(timezone.utc),
            'error': str(e),
            'status': HTTPStatus.BAD_REQUEST
        })
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        g.db.requests.insert_one({
            'location': location,
            'timestamp': datetime.now(timezone.utc),
            'error': str(e),
            'status': HTTPStatus.INTERNAL_SERVER_ERROR
        })
        return jsonify({'error': str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

@bp.route('/requests', methods=['GET'])
def get_requests():
    try:
        limit = request.args.get('limit', default=10, type=int)
        if limit < 1:
            return jsonify({'error': 'Limit must be at least 1'}), HTTPStatus.BAD_REQUEST

        # Fetch most recent requests, sorted by timestamp ascending
        recent_requests = g.db.requests.find().sort('timestamp', -1).limit(limit)
        
        # Convert MongoDB documents to JSON-serializable format
        requests_list = [
            {
                'location': req['location'],
                'timestamp': req['timestamp'].isoformat(),
                'response': req.get('response'),
                'error': req.get('error'),
                'status': req['status']
            }
            for req in recent_requests
        ]
        
        return jsonify({'requests': requests_list}), HTTPStatus.OK
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR