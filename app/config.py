from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
    NOAA_API_TOKEN = os.getenv('NOAA_API_TOKEN', 'your-default-secret-key')