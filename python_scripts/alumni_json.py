import os
import csv
import json

batch = "e02"
dataFile = open("../_csv/"+batch+".csv", 'r')


csvFile = csv.reader(dataFile)
data = {}

for line in csvFile:
    print(line)
    eNumber = line[2]
    nameInitials = line[0] + line[1]
    profile = "images/students/default.jpg"

    print(eNumber, nameInitials, profile)

    data[eNumber] = { 'reg_no': eNumber, 'name_with_initials': nameInitials, 'image_url': profile }


filename = "../_data/stud/{0}.json".format(batch)
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as f:
    f.write(json.dumps(data, indent = 4))
