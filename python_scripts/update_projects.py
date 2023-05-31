# Update the Project information from the Publication API, pre-process and
# link with the student and staff profile pages

# Author: E/15/150 Nuwan Jaliyagoda - nuwanjaliyagoda@eng.pdn.ac.lk

import requests
import os
import json

try:
    url = "https://api.ce.pdn.ac.lk/projects/v1/filter/students/index.json"
    r = requests.get(url)

    if r.status_code==200:
        # it is available
        stud_projects = json.loads(r.text)
        filename = "../_data/student_projects.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write(json.dumps(stud_projects, indent = 4))

        print("Students: Success")
    else:
        print("Students: Failed")

except:
    print('parse failed; ' +  url)

try:
    url = "https://api.ce.pdn.ac.lk/projects/v1/filter/staff/index.json"
    r = requests.get(url)

    if r.status_code==200:
        # it is available, group by batch
        staff_projects = json.loads(r.text)
        grouped_proj = {}

        for s in staff_projects:
            if s not in grouped_proj:
                grouped_proj[s] = { 'count': 0, 'projects': {} }

            for p in staff_projects[s]:
                batch = p['project_url'].split('/')[4]
                cat = p['project_url'].split('/')[3]
                
                if cat == "4yp":
                    grouped_proj[s]['count'] = grouped_proj[s]['count'] + 1 

                    if batch in grouped_proj[s]['projects']:
                        grouped_proj[s]['projects'][batch].append(p)
                    else:
                        grouped_proj[s]['projects'][batch] = [p]
                    
        filename = "../_data/staff_projects.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write(json.dumps(grouped_proj, indent = 4))

        print("Staff: Success")
    else:
        print("Staff: Failed")

except:
    print('parse failed; ' +  url)
