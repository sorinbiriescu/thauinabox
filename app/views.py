from app import app
from flask import render_template, request, redirect, url_for
import json
import os

script_dir = os.path.dirname(__file__)

@app.route("/")
@app.route('/index')
def index():
    """ Main page / index"""
    return render_template('index.html')

@app.route("/resume")
def resume():
    resume_json = open(os.path.join(script_dir, 'static/json/resume.json'), 'r')
    resume_content = json.loads(resume_json.read().encode('utf-8'))
    jobs=resume_content['work_experience']
    education = resume_content['education']
    languages = resume_content['languages']
    competences = resume_content['competences']
    
    competence_categories = {}
    for k,v in competences.items():
        if v['type'] in competence_categories.keys():
            if v['category'] in competence_categories[v['type']]:
                continue
            else:
                competence_categories[v['type']].append(v['category'])
        else:
            competence_categories[v['type']] = []
            competence_categories[v['type']].append(v['category'])

    content = {
        "jobs":jobs,
        "education":education,
        "languages":languages,
        "competences":competences,
        "competence_categories":competence_categories
    }  

    return render_template('resume.html', ** content)

@app.route("/leisure")
def leisure():
    return render_template('leisure.html')
