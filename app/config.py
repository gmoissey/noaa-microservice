from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://mongo:27017/weather_api_db')