from flask import Flask, render_template
from requests import get
from threading import Thread

API_URL = 'http://api.weatherapi.com/v1/current.json?key=accca51b4f3e479d8fb164459241802&q=Mexico&aqi=no'
app = Flask(__name__)

name = ''
region = ''
country = ''
localtime = ''
tempc = ''
tempf = ''
lastupdated = ''

## Funcion que llame a una API y traiga algun dato
def getWeather():
    global name
    global region
    global country
    global localtime
    global tempc
    global tempf
    global lastupdated
    
    resp = get(API_URL).json()
    resp = dict(resp)

    # main objects
    location = resp['location']
    current = resp['current']

    # Location attributes
    name = location['name']
    region = location['region']
    country  = location['country']
    localtime = location['localtime']
    
    # Current attributes
    tempc = current['temp_c']
    tempf = current['temp_f']
    lastupdated = current['last_updated']


@app.route('/')
def hello_world():
    ## Hilo que cada segundo llame a esa funcion
    weatherThread = Thread(target=getWeather)
    weatherThread.start()
    weatherThread.join()
    # Customizar el html
    return render_template(
        './index.html',
        name=name,
        region=region,
        country=country,
        localtime=localtime,
        tempc=tempc,
        tempf=tempf,
        lastupdated=lastupdated
    )

if __name__=='__main__':
    app.run()

