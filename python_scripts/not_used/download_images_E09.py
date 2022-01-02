# Download images for E09 from https://cepdnaclk.github.io/department-website-2013/

# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk

import json
import urllib.request

e09json = open("../_data/stud/e09.json", "r")
data = json.load(e09json)
for student in data:
    regNo = str(student.split("/")[-1])
    print(regNo)
    imageLink = f"https://cepdnaclk.github.io/department-website-2013/people/images/e09/e09{regNo}.jpg"
    urllib.request.urlretrieve(imageLink, f"../images/students/e09/e09{regNo}.jpg")

