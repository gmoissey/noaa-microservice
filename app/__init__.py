from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Import and register routes
    from .routes import weather_api
    app.register_blueprint(weather_api.bp)
    
    return app