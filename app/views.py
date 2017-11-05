from app import app
from flask import render_template, request, redirect, url_for

@app.route('/')
@app.route('/index')

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/work-timeline")
def work_timeline():
    return render_template('work-timeline.html')