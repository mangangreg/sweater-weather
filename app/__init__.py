import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Config
HERE = Path(__file__).resolve().parent
load_dotenv(HERE/'.env')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['PGRES_URI']
db_meta = MetaData(schema=os.environ['PGRES_SCHEMA'])
db = SQLAlchemy(app, metadata=MetaData(schema='weatherapp'))

from app import routes
from app import models