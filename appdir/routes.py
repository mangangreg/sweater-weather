import requests
from flask import jsonify, request
from appdir import app, db
from appdir import weather_api

@app.route('/', methods=['GET'])
def index():
    return jsonify({'success': True, 'msg': "Not another weather app"})


@app.route('/api/weather/current', methods=['GET'])
def weather_current():
    ''' Get the current weather, for given lat and lon'''

    lat = request.args.get('lat', None)
    lon = request.args.get('lon', None)
    res = weather_api.get_weather_current(lat=lat, lon=lon)

    return res

@app.route('/api/weather/daily', methods=['GET'])
def weather_daily():
    ''' Get the current weather, for given lat and lon'''

    lat = request.args.get('lat', None)
    lon = request.args.get('lon', None)
    res = weather_api.get_weather_daily(lat=lat, lon=lon)

    return jsonify(res)