import csv
import json

"""
This is to simply transform the Casual Instructor information into JSON
Example CSV Format:
    Name,GP106,CO224,CO225,CO226,CO253,CO326,CO327,CO328,Email
    JohnDoe,0,0,0,0,0,1,1,0,e17296@eng.pdn.ac.lk
"""


def getENumberFromEmail(email):
    return "E/{}/{}".format(email[1:3], email[3:6])


# Create the following file before run the script
filename = "./casual_instructors.csv"

data = []
with open(filename, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

courses = [
    "CO221",
    "CO222",
    "CO223",
    "CO321",
    "CO322",
    "CO323",
    "CO324",
    "CO325",
    "CO3070",
    "GP106",
    "CO224",
    "CO225",
    "CO226",
    "CO253",
    "CO326",
    "CO327",
    "CO328",
]
stud_list = []

for row in data:
    stud_courses = []
    for c in courses:
        if c in row and row[c] == "1":
            stud_courses.append(c)

    stud_list.append(
        {
            "eNumber": getENumberFromEmail(row["Email"]),
            "name": row["Name"],
            "position": ", ".join(stud_courses),
        }
    )

with open("./casual_instructors.json", "w") as file:
    json.dump(stud_list, file, indent=2)
