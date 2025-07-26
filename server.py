""" This file is part of the Python Lab project. "Get Started with Flask Basics" """
#importing Flask
from flask import Flask, jsonify

#creating a Flask application instance
app = Flask(__name__)

#defining a route for the root URL
@app.route('/')
def home():
    #function to handle requests to the root URL
    return jsonify({ "message": "Hello, Flask!" })


