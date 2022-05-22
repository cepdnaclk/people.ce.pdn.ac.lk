# Update the Publication information from the Publication API, pre-process and
# link with the student and staff profile pages

# Author: E/15/150 Nuwan Jaliyagoda - nuwanjaliyagoda@eng.pdn.ac.lk

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
        staff_pub_year = {}

        # pre-process the data
        for staff in staff_pub:
            pub_count = 0
            year_count = 0

            if staff not in staff_pub_year: staff_pub_year[staff]= {
                "publication_count": 0, "year_count": 0, "publications": {}
            }

            for pub in staff_pub[staff]:
                pub_count += 1
                year = pub['year']

                if year not in staff_pub_year[staff]["publications"]: staff_pub_year[staff]["publications"][year] = []
                staff_pub_year[staff]["publications"][year].append(pub)

            staff_pub_year[staff]['publication_count'] = pub_count
            staff_pub_year[staff]['year_count'] = len(staff_pub_year[staff]["publications"])

        # Write into the file
        filename = "../_data/staff_publications.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write(json.dumps(staff_pub_year, indent = 4))

        print("Staff: Success")

    else:
        print("Staff: Failed")

except:
    print('parse failed; ' +  url)
