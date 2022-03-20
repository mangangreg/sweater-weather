import requests
from flask import jsonify
from app import app

@app.route('/', methods=['GET'])
def index():
    return jsonify({'success': True, 'msg': "Not another weather app"})
