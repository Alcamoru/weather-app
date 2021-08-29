import json
import sys

import requests
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def add_city():
    city_name = request.form["city_name"]
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}"
                     f"&appid=58058341b60d9730423df34082a652e2")
    weather_data: dict = json.loads(r.content)
    data = {"temp": int(weather_data["main"]["temp"]) - 273, "city": city_name, }

    return render_template('index.html', weather=data)


# don't change the following way to run flask:
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
