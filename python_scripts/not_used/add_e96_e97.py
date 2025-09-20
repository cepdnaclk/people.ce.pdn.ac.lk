import json

import pandas as pd

df = pd.read_csv("input.csv")

# ENo, name, email address and country

jsonObject = {}

for row in df.iterrows():
    row = row[1]
    reg_no = row["Your Registration Number"].upper()
    name = row["Your Name"]
    email = row["Your Email Address"]
    country = row["Your current country of residence"]

    if len(str(reg_no)) == 0:
        continue
    isSkip = True
    if "E/96" in reg_no:
        isSkip = False
    # if"E/97" in reg_no:
    #     isSkip = False

    if isSkip:
        continue

    jsonObject[reg_no] = {}
    jsonObject[reg_no]["reg_no"] = reg_no
    jsonObject[reg_no]["name_with_initials"] = name.title()
    jsonObject[reg_no]["image_url"] = "images/students/default.jpg"
    jsonObject[reg_no]["page_url"] = f"/students/e96/{int(reg_no.split('/')[2]):03d}/"

jsonObject = dict(sorted(jsonObject.items()))
with open("../../_data/stud/e96.json", "w") as f:
    f.write(json.dumps(jsonObject, indent=2))


#     pageContent = f"""---
# layout: studentDetails
# permalink: "/students/e{reg_no.split("/")[1]}/{int(reg_no.split("/")[2]):03d}/"
# title: {name}

# reg_no: {reg_no}
# batch: E{reg_no.split("/")[1]}

# department: "Computer Engineering"
# current_affiliation: #

# full_name: #
# name_with_initials: {name}
# preferred_short_name: #
# preferred_long_name: #
# honorific: Mr.

# email_faculty: {email}
# email_personal: {email}

# location: {country}

# url_cv: #
# url_website: #
# url_linkedin: #
# url_github:
# url_facebook:
# url_researchgate:
# url_twitter:

# interests: #

# image_url: "images/students/default.jpg"
# ---"""

#     with open(f"../../pages/students/e97/e97{reg_no.split('/')[2]}.html",'w') as f:
#         f.write(pageContent)
