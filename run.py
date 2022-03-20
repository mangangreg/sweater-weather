from appdir import app, db
from appdir.models import User, openweather_response, weather
from appdir import weather_api
import os
from importlib import reload

@app.shell_context_processor
def make_shell_context():

    context = {
        'db': db, 
        'User': User, 
        'weather':weather, 
        'openweather_response': openweather_response,
        'wapi': weather_api,
        'reload': reload
    }
    print(f"Importing: {', '.join(context.keys())}")
    return context

if __name__ == '__main__' and not os.environ.get('DONT_RUN'):
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=5000)