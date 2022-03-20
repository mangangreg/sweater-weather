from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime
import os
import requests

from app.models import weather, openweather_response
from app import db

HERE = Path(__file__).resolve().parent
load_dotenv(HERE/'.env')

BASE_URL = "http://api.openweathermap.org/data/2.5"
WEATHER_URL = BASE_URL + '/weather?'
ONE_CALL_URL = BASE_URL + '/onecall?'

TOKEN = os.environ['OPEN_WEATHER_TOKEN']
DEFAULT_LOCATION = os.environ['DEFAULT_LOCATION']
DEFAULT_LAT = float(os.environ['DEFAULT_LAT'])
DEFAULT_LON = float(os.environ['DEFAULT_LON'])

KtoC = lambda kelvin: kelvin - 273.15

def get_weather(location=DEFAULT_LOCATION):
    resp = requests.get(WEATHER_URL, params={'q': location, 'appid': TOKEN})
    if resp.ok:
        return resp.json()
    else:
        raise ValueError(f'OpenWeather API returned {resp.status_code}')

def get_onecall(lat=DEFAULT_LAT, lon=DEFAULT_LON):
    one_call_params = {
        'lat': lat,
        'lon': lon,
        'appid': TOKEN
    }
    response = requests.get(ONE_CALL_URL, params=one_call_params)
    if response.ok:
        return response.json()
    else:
        raise ValueError(f'OpenWeather API returned {response.status_code}')
    
    
def parse_onecall(resp):
    lat, lon = resp['lat'], resp['lon']
    tsamp_retrieved = datetime.fromtimestamp(resp['current']['dt'])
    
    obj = {'weather':[]}
    
    for period in ['minutely', 'hourly', 'daily']:
        obj['weather'].extend([
            {
                
                'lat': lat,
                'lon': lon,
                'period': period,
                'retrieved_at': tsamp_retrieved,
                'timestamp': entry['dt'],
                'response': entry
            }
            for entry in resp[period]
        ])
    obj['weather'].append(
            {
                
                'lat': lat,
                'lon': lon,
                'period': 'current',
                'retrieved_at': tsamp_retrieved,
                'timestamp': resp['current']['dt'],
                'response': resp['current']
            }
        )
        
    return obj

def update():
    wres = db.session.query(openweather_response).first()
    parsed = parse_onecall(wres.response)
    for row in parsed['weather']:
        obj = weather(**row, api_response_id=wres.id)
        db.session.add(obj)
    db.session.commit()

#     pass