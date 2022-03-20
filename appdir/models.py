from datetime import datetime

from appdir import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

class openweather_response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tstamp = db.Column(db.DateTime, default=datetime.now())
    endpoint = db.Column(db.String(200), nullable=False)
    response = db.Column(db.JSON, nullable=False)
    weather_children = db.relationship('weather')

class weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    period = db.Column(db.String, nullable=False)
    retrieved_at = db.Column(db.DateTime, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now())
    api_response_id = db.Column(db.Integer, db.ForeignKey('openweather_response.id'))
    response = db.Column(db.JSON, nullable=False)

    def as_dict(self):
        return _as_dict_(self)

def _as_dict_(row):
    return {k:v for k,v in row.__dict__.items() if not k.startswith('_')}