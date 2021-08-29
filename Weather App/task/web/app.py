from flask import Flask
from flask import render_template
from flask import request
import sys

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def add_city():
    city_name = request.form["city_name"]
    print(city_name)
    return render_template('index.html')


# don't change the following way to run flask:
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
