# -*- coding: utf-8 -*-

from moonfish import app
from flask import request, jsonify, render_template


@app.route('/', methods=['GET'])
def home():
    return 'Connection Success'