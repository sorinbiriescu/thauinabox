from app import app
from flask import render_template, request, redirect, url_for

@app.route('/')
@app.route('/index')

@app.route("/")
def hello():
    return render_template('index.html')