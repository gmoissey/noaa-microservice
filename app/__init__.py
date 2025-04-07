from flask import Flask, g
from flask_cors import CORS
from pymongo import MongoClient
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    
    # MongoDB setup
    mongo_uri = app.config.get('MONGO_URI', 'mongodb://mongo:27017/weather_api_db')  # Fallback if not in Config
    mongo_client = MongoClient(mongo_uri)
    db = mongo_client['weather_api_db']

    # Make db available to routes/services via app context
    @app.before_request
    def inject_db():
        g.db = db

    # Import and register routes
    from .routes import weather_api
    app.register_blueprint(weather_api.bp)
    
    return app