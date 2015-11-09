#!/usr/bin/env python
# encoding: utf-8

import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
        return 'Hello World!'
