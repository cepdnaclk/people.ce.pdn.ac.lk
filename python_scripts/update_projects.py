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
        # it is available
        staff_projects = json.loads(r.text)
        filename = "../_data/staff_projects.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write(json.dumps(staff_projects, indent = 4))

        print("Staff: Success")
    else:
        print("Staff: Failed")

except:
    print('parse failed; ' +  url)
