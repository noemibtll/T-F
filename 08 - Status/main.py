from flask import Flask, render_template
from requests import get
from threading import Thread

app = Flask(__name__)

weather_data = {}

def get_weather():
    global weather_data
    API_KEY = 'accca51b4f3e479d8fb164459241802'
    API_URL = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Mexico&aqi=no'
    
    resp = get(API_URL).json()
    location = resp.get('location', {})
    current = resp.get('current', {})
    
    weather_data = {
        'name': location.get('name', ''),
        'region': location.get('region', ''),
        'country': location.get('country', ''),
        'localtime': location.get('localtime', ''),
        'tempc': current.get('temp_c', ''),
        'tempf': current.get('temp_f', ''),
        'lastupdated': current.get('last_updated', '')
    }

@app.route('/')
def hello_world():
    weatherThread = Thread(target=get_weather)
    weatherThread.start()
    weatherThread.join()
    
    global weather_data
    return render_template('./index.html', **weather_data)

@app.route('/historial')
def historial():
    global weather_data
    return render_template('historial.html', **weather_data)

if __name__ == '__main__':
    app.run()
