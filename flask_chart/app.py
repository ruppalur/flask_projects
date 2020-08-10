#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2019, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __license__ = "MIT"
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"

from flask import Flask, Response, render_template
from datetime import datetime
import time
import psutil
import json
import random


app = Flask(__name__)


# page which listens to the '/cpuinfo' and render to the chart.
@app.route('/cpudata')
def cpudata():
    return render_template('cpudata.html')

# page creates json data and send the data over SSE.


@app.route('/cpuinfo')
def cpu_info_data():
    def get_cpu():
        while True:
            output = json.dumps({'time': datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"), 'cpu0': psutil.cpu_percent(percpu=True, interval=1)[0], 'cpu1': psutil.cpu_percent(percpu=True, interval=1)[1]})
            yield f"data:{output}\n\n"
            time.sleep(1)

    return Response(get_cpu(), mimetype='text/event-stream')


# home page for the chart, reference from the Ron page
@app.route('/')
def index():
    return render_template('index.html')


# sample route for the chart data, reference from the ron page.
@ app.route('/chart-data')
def chart_data():
    def generate_random_data():
        while True:
            json_data = json.dumps(
                {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': random.random() * 100})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    return Response(generate_random_data(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
