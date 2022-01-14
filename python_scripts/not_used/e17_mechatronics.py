## Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk
import urllib.request
e17mech = """E/17/064
E/17/388
E/17/035
E/17/156
E/17/259
E/17/004
E/17/024
E/17/008
E/17/286
E/17/053""".split("\n")

feelsAll = open("../_csv/FEeLS_all.txt")
regNoImageLink = {}
regNoNameDICT = {}
for line in feelsAll:
    regNoImageLink[line.split()[0]] = line.split()[-1]
    regNoNameDICT[line.split()[0]] = " ".join(line.split()[1:-2])

for each in e17mech:
    regNo = each[-3:]

    urllib.request.urlretrieve(
        regNoImageLink[each], f"../images/students/e17/e17{regNo}.jpg")
    htmlFile = open(f"../pages/students/e17/e17{regNo}.html", "w")
    text = f"""---
layout: studentDetails
permalink: "/students/e17/{int(regNo):03d}/"
title: Abeywickrama A.K.D.A.S.

reg_no: E/17/{int(regNo):03d}
batch: E17

department: Mechanical
current_affiliation: Department of Mechanical Engineering, University of Peradeniya

full_name: {regNoNameDICT[each].title()}
name_with_initials: {regNoNameDICT[each].title()}
preferred_short_name: {regNoNameDICT[each].title()}
preferred_long_name: #
honorific: #

email_faculty: e17{int(regNo):03d}@eng.pdn.ac.lk
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

image_url: "images/students/e17/e17{regNo}.jpg"
---
    """
    htmlFile.write(text)
    htmlFile.close()
