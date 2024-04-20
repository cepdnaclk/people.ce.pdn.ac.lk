# by E18098

import pandas as pd
import json

# Read the data
df = pd.read_csv("data.csv")

# read json
with open("../badges/casual_instructors_2024.json", "r") as f:
    data = json.load(f)

for each in df.iterrows():
    regno = each[1]["Reg. No."]
    name = each[1]["Preferred Name"]
    courses = each[1]["Assigned Course(s)"].split(",")
    # strip each element in courses
    courses = [course.strip() for course in courses]


    data["students"].append({"eNumber": regno, "name": name, "position": ", ".join(courses)})

# write json
with open("../badges/casual_instructors_2024.json", "w") as f:
    json.dump(data, f, indent=4)
