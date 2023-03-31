from flask import Flask, render_template, request
import glob
import random
# -*- coding: utf-8 -*-

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


app.run(debug=True)