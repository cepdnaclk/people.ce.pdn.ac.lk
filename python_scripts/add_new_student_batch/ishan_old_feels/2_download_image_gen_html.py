# Download images from FEeLS and generate profile pages html for the new batch
# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk

# import urllib.request

batch_ComputerEngOnly = open("./ComputerEngOnly.txt", "r")
CO = {}
for each in batch_ComputerEngOnly:
    CO[each.strip()] = "blank"  # name is not required here. it wil be taken from the other file

batch_allStudents = open("./batch_all.txt", "r")
for each in batch_allStudents:
    name = each.split("https")[0].replace("\t", " ")
    link = "https" + each.split("https")[1]
    regNo = name[0:8]
    name = name[8:-2]
    # print(f"'{regNo}'")
    if regNo in CO.keys():
        name = name.strip().title().replace("Miss", "").replace("Mr", "")
        # link = link.strip()
        regNo = "".join(regNo.split("/")[1:])
        # print(link)
        # urllib.request.urlretrieve(link, f"../../images/students/e19/e{regNo}.jpg")
        htmlFile = open(f"../../pages/students/e20/e{int(regNo):03d}.html", "w")
        text = f"""---
layout: studentDetails
permalink: "/students/e20/{int(regNo[2:]):03d}/"
title: will be filled by GH action


reg_no: E/20/{int(regNo[2:]):03d}
batch: E20

department: Computer Engineering
current_affiliation: Department of Computer Engineering, University of Peradeniya

full_name: {name}
name_with_initials: {name}
preferred_short_name: {name}
preferred_long_name: #
honorific: #

email_faculty: e20{int(regNo[2:]):03d}@eng.pdn.ac.lk
email_personal: #

location: #

url_cv: #
url_website: #
url_linkedin: #
url_github: #
url_facebook: #
url_researchgate: #
url_twitter: #

interests: #

image_url: "images/students/e20/e{regNo}.jpg"

---
        """
        htmlFile.write(text)
        htmlFile.close()
