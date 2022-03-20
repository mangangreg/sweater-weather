from app import app, db
from app.models import User, openweather_response, weather
from app import weather_api
import os

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'weather':weather, 
    'openweather_response': openweather_response,
    'wapi':weather_api}

if __name__ == '__main__' and not os.environ.get('DONT_RUN'):
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=5000)