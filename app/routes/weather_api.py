from flask import Blueprint, jsonify, request

bp = Blueprint('weather-api', __name__, url_prefix='/weather-api')

@bp.route('/location/<location>', methods=['GET'])
def get_weather(location):
    return jsonify({'location': location}), 200

@bp.route('/requests', methods=['GET'])
def get_requests():
    return jsonify({'requests': 'success'}), 200