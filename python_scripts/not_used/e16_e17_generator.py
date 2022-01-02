import os

dataFile = open("./_csv/e16_e17.txt", 'r')

# have to change some things based on e16 or 17
path = "./images/students/e17/"
directory_list = os.listdir(path)
existingImages = []
for each in directory_list:
    each = each.split(".")[0][1:]
    existingImages.append(each)

for line in dataFile:
    name = " ".join(line.split(":")[0].split())
    regNo = "".join(name.split()[0].split("/")[1:])
    name = " ".join(name.split()[1:]).title()

    if regNo in existingImages:
        print(regNo)
        htmlFile = open(f"./pages/students/e17/e{int(regNo):03d}.html", "w")
        text = f"""---
layout: studentDetails
permalink: "/students/e17/{int(regNo[2:]):03d}/"

reg_no: E/17/{int(regNo[2:]):03d}
batch: E17

full_name: {name}
name_with_initials: {name}
preferred_short_name: {name}
preferred_long_name: #
honorific: #

email_faculty: e17{int(regNo[2:]):03d}@eng.pdn.ac.lk
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
image_url: "images/students/e17/e{regNo}.jpg"
---
        """
        htmlFile.write(text)
        htmlFile.close()
