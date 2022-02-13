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
        print("Success")
    else:
        print("Failed")

except:
    print('parse failed; ' +  url)
