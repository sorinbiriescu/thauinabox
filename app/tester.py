import json
import os

script_dir = os.path.dirname(__file__)

work_experience_json = open(os.path.join(script_dir, 'static/json/resume.json'),'r')
jobs = json.loads(work_experience_json.read())

competences = jobs['competences']
print(competences)

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

for k,v in competence_categories.items():
    print(k,v)