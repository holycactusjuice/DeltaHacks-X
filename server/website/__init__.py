from flask import Flask
from flask_login import LoginManager
from pymongo import MongoClient
from flask_pymongo import PyMongo
from flask_cors import CORS
import os
from dotenv import load_dotenv
import os
from openai import OpenAI

openAI_client = OpenAI(
    api_key="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"
)
load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')
MONGODB_KEY = os.getenv('MONGODB_KEY')
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.urandom(32)

    # configure CORS to allow requests from frontend
    # allow cookies so that session can be used
    CORS(app, resources={
         r"/api/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

    from .views import views
    # from .auth import auth

    app.register_blueprint(views, url_prefix='/')

    return app
