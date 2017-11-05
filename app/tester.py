import json
import os

script_dir = os.path.dirname(__file__)

work_experience_json = open(os.path.join(script_dir, 'static/json/work_experience.json'),'r')
jobs = json.loads(work_experience_json.read())

for i in jobs:
    print(jobs[i]['job_title'])

