from app import app
from flask import render_template, request, redirect, url_for
import json
import os

script_dir = os.path.dirname(__file__)

@app.route('/')
@app.route('/index')

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/resume")
def resume():
    resume_json = open(os.path.join(script_dir, 'static/json/resume.json'),'r')
    resume_content = json.loads(resume_json.read().encode('utf-8'))
    return render_template('resume.html',jobs=resume_content['work_experience'])

@app.route("/leisure")
def leisure():
    return render_template('leisure.html')