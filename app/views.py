from app import app
from flask import render_template, request, redirect, url_for

@app.route('/')
@app.route('/index')

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/resume")
def resume():
    return render_template('resume.html')

@app.route("/leisure")
def leisure():
    return render_template('leisure.html')