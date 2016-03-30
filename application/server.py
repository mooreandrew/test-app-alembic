from application import app
import os
from flask import Flask

@app.route('/')
def index():
    return(app.config['TESTVALUE'])
