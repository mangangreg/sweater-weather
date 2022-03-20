import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import MetaData

# Config
HERE = Path(__file__).resolve().parent
load_dotenv(HERE/'.env')

app = Flask(__name__)
# TODO: set up a config class
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['PGRES_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database
db_meta = MetaData(schema=os.environ['PGRES_SCHEMA'])
db = SQLAlchemy(app, metadata=MetaData(schema='weatherapp'))

# Cors policy for local development
# TODO: do this with env variables
cors = CORS(app,
    resources={r'*': {'origins': "http://localhost:8080"}},
    expose_headers=["Content-Type", "X-CSRFToken"],
    supports_credentials=True
)

# TODO: implement login manager
# login = LoginManager(app)

from appdir import routes
from appdir import models