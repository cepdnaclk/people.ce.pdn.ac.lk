import requests
import os
import json

# Get student publications
try:
    url = "https://api.ce.pdn.ac.lk/publications/v1/filter/students/index.json"
    r = requests.get(url)

    if r.status_code==200:
        # it is available
        stud_pub = json.loads(r.text)
        filename = "../_data/student_publications.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write(json.dumps(stud_pub, indent = 4))
        print("Student: Success")
    else:
        print("Student: Failed")

except:
    print('parse failed; ' +  url)

# Get staff publications
try:
    url = "https://api.ce.pdn.ac.lk/publications/v1/filter/staff/index.json"
    r = requests.get(url)

    if r.status_code==200:
        # it is available
        staff_pub = json.loads(r.text)
        filename = "../_data/staff_publications.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write(json.dumps(staff_pub, indent = 4))
        print("Staff: Success")
    else:
        print("Staff: Failed")

except:
    print('parse failed; ' +  url)
