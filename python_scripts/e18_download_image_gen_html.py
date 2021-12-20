## Download images from FEeLS and generate E18 profile pages html
## Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk

import urllib.request

e18_CO = open("./_csv/e18_CO.txt", "r")
CO = {}
for each in e18_CO:
    each = each.split("Student")[0].strip()
    regNo = each[0:8]
    name = each[8:]
    CO[regNo] = name

e18_all = open("./_csv/e18_all.txt", "r")
for each in e18_all:
    name = each.split("https")[0].replace("\t", " ")
    link = "https" + each.split("https")[1]
    regNo = name[0:8]
    name = name[8:-2]
    if regNo in CO.keys():
        name = name.strip().title()
        link = link.strip()
        regNo = "".join(regNo.split("/")[1:])
        print(link)
        urllib.request.urlretrieve(link, f"images/students/e18/e{regNo}.jpg")

        htmlFile = open(f"./pages/students/e18/e{int(regNo):03d}.html", "w")
        text = f"""---
layout: studentDetails
permalink: "/students/e18/{int(regNo[2:]):03d}/"

reg_no: E/18/{int(regNo[2:]):03d}
batch: E18

full_name: {name}
name_with_initials: {name}
preferred_short_name: {name}
preferred_long_name: #
honorific: #

email_faculty: e18{int(regNo[2:]):03d}@eng.pdn.ac.lk
email_personal: #

location: #

url_cv: #
url_website: #
url_linkedin: #
url_github: #
url_facebook: #
url_researchgate: #
url_twitter: #

projects_done: []
image_url: "images/students/e18/e{regNo}.jpg"
---
        """
        htmlFile.write(text)
        htmlFile.close()
