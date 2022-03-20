from datetime import datetime

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repre__(self):
        return f"<User {self.username}>"

class openweather_response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tstamp = db.Column(db.DateTime, default=datetime.now())
    endpoint = db.Column(db.String(200), nullable=False)
    response = db.Column(db.JSON, nullable=False)
    weather_children = db.relationship('weather')

class weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.now())
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    period = db.Column(db.String, nullable=False)
    retrieved_at = db.Column(db.DateTime, nullable=False)
    api_response_id = db.Column(db.Integer, db.ForeignKey('openweather_response.id'))
    response = db.Column(db.JSON, nullable=False)
