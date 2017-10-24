from app import app
from flask import render_template, request, redirect, url_for

@app.route('/')
@app.route('/index')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/timeline")
def timeline():
    return render_template('timeline.html')