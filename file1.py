#!/usr/bin/env/ python3
import psutil
from flask import Flask, jsonify
app=Flask(__name__)
@app.route('/')
def startowa():
    return 'Strona startowa'
@app.route('/version')
def check_ver():
    return 'Version: [0.21]'
@app.route('/cpu/', methods=['GET'])
def cpu_info():
    cpus = [
        {'liczba cpu':psutil.cpu_count()},
        {'statyski cpu':psutil.cpu_stats()}
    ]
    return jsonify(cpus)
if __name__ == '__main__':
    app.run(host='0.0.0.0')