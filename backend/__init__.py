from os import getenv
from dotenv import load_dotenv
from flask import Flask
# from flask_mail import Mail, Message
# from flask_cors import CORS

from .utils import WeatherApiETL

load_dotenv()

app = Flask(__name__)
etl = WeatherApiETL(api_key=getenv("API_KEY"))
# print(etl.api_key)
# exit()
# CORS(app)
from . import routes

if __name__ == "__main__":
    app.run(debug=int(getenv("DEBUG")), port=int(getenv("PORT")))