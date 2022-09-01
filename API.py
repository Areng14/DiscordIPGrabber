from flask import Flask, jsonify
from threading import Thread
from flask_restful import Resource, Api
import json
import random

app = Flask('')
api = Api(app)

blacklistedID = {"819069345778122": "1"}


@app.route('/')
def home():
    return "API Up and running!"


@app.route('/invalidid', methods=['GET'])
def testing():
    openfile = open("data.json", "r")
    VA = openfile.read()
    returnthis = VA.replace('"', "")
    return jsonify(returnthis)


@app.route('/validall', methods=['GET'])
def validall():
    openfile = open("data2.json", "r")
    VB = openfile.read()
    returnthis = VB.replace('"', "")
    return jsonify(returnthis)


def run():
    app.run(host='0.0.0.0', port=7210)


t = Thread(target=run)
t.start()
