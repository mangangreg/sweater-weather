from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime
import os
import requests

from appdir.models import weather, openweather_response
from appdir import db

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

## Fetch from OpenWeather

def fetch_weather(location=DEFAULT_LOCATION):
    resp = requests.get(WEATHER_URL, params={'q': location, 'appid': TOKEN})
    if resp.ok:
        return resp.json()
    else:
        raise ValueError(f'OpenWeather API returned {resp.status_code}')

def fetch_onecall(lat=DEFAULT_LAT, lon=DEFAULT_LON):
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

def fetch_latest_onecall():
    resp = fetch_onecall()

    new_entry = openweather_response(endpoint=ONE_CALL_URL, response=resp)
    db.session.add(new_entry)
    db.session.commit()

    ret = {
        'timestamp': new_entry.tstamp,
        'response': resp
    }
    return ret

    
def parse_onecall(resp):
    ''' Parse the response of a query to the openweather onecall api'''
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
                'timestamp': datetime.fromtimestamp(entry['dt']),
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
                'timestamp': tsamp_retrieved,
                'response': resp['current']
            }
        )
        
    return obj

def parse_all():
    ''' 
    Find all unparsed openweather responses and parse them,
    creating new entries in the weather table
    '''

    # TODO: work out the sqlalchemy way of doing this query
    q = '''
           select dw.*, r.id, r.response
             from weatherapp.openweather_response r
        left join (select distinct api_response_id from weatherapp.weather ) dw 
                      on dw.api_response_id = r.id 
            where dw.api_response_id is null
    '''
    res = db.session.execute(q)
    for ret_row in res:
        print(type(ret_row), ret_row.id)

        parsed = parse_onecall(ret_row.response)
        for row in parsed['weather']:
            obj = weather(**row, api_response_id=ret_row.id)
            db.session.add(obj)
        db.session.commit()


## Queries
def get_weather_current(lat=DEFAULT_LAT, lon=DEFAULT_LON):

    lat = lat or DEFAULT_LAT
    lon = lon or DEFAULT_LON
    print(f'Getting weather for {lat=}{lon=}')
    
    #TODO implement lat/lon filter
    wrow = db.session.query(weather) \
        .filter(weather.period=='current') \
        .order_by(weather.timestamp.desc()).first()

    return wrow.as_dict()

def get_weather_daily(lat=DEFAULT_LAT, lon=DEFAULT_LON):

    q = '''
           select *
             from weatherapp.weather w
            where period='daily' 
                and retrieved_at=(select max(retrieved_at) from weatherapp.weather)
    '''
    res = db.session.execute(q)
    return [dict(x) for x in res]


# def get_weather(period='current', lat=DEFAULT_LAT, lon=DEFAULT_LON):
#     wrow = db.session.query(weather) \


#     return wrow.as_dict()