# Update student profile pictures using the data taken from Google Form
# Form URL - https://forms.gle/s2otrv1ifh7kQ3oD9 Owned by: e18098@eng.pdn.ac.lk

# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk

import requests
import os
import gdown  # pip install gdown

googleFromCSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRItS_wC2tPxeUxXgI_C-5a5HCn4_sFFTRnG1MVnQgnWIy126Afa2e1oKt-_Z5HO17zq2tHoqwDLQVb/pub?output=csv"
googleFromCSV = requests.get(googleFromCSV, headers={
                             'Cache-Control': 'no-cache'}).text.split("\n")

# Index of the CSV parameters
TIMESTAMP = 0
EMAIL = 1
DEPARTMENT = 2
FULL_NAME = 3
NAME_WITH_INITIALS = 4
PREFERRED_SHORT_NAME = 5
PREFERRED_LONG_NAME = 6
HONORIFIC = 7
FACULTY_EMAIL = 8
PERSONAL_EMAIL = 9
LOCATION = 10
URL_CV = 11
URL_PERSONAL = 12
URL_LINKEDIN = 13
URL_GITHUB = 14
URL_FB = 15
URL_RESEARCHGATE = 16
URL_TWITTER = 17
INTERESTS = 18
URL_IMAGE = 19

if __name__ == "__main__":
    for eachLine in googleFromCSV:
        studentData = eachLine.split(",")

        if ":" not in studentData[0]:
            # if there is no data in this line or this is the header line
            continue

        print("Processing: " + studentData[EMAIL])
        # get batch and regNo
        batch = studentData[EMAIL][1:3]  # 18
        regNo = studentData[EMAIL][3:6]  # 098

        permalink = f"/students/e{batch}/{regNo}"

        # get department
        deparment = ""
        if studentData[DEPARTMENT] == "Department of Computer Engineering":
            deparment = "Computer"
        elif studentData[DEPARTMENT] == "Department of Mechanical Engineering":
            deparment = "Mechanical"
        elif studentData[DEPARTMENT] == "Department of Manufacturing & Industrial Engineering":
            department = "Manufacturing"

        # current affiliation
        current_affiliation = "Department of Computer Engineering, University of Peradeniya"

        # interests
        interests = ",".join(studentData[INTERESTS].split(";"))

        # image
        image_path = f"images/students/e{batch}/e{batch}{regNo}.jpg"
        try:  # delete if image exists
            os.remove("../"+image_url)
            print("Existing image deleted")
        except:
            pass
        gdown.download("https://drive.google.com/uc?id=" +
                       studentData[URL_IMAGE].split("=")[1], "../"+image_path, quiet=False)

        outputString = f"""---
layout: studentDetails
permalink: "/students/e{batch}/{regNo}/"
title: {studentData[NAME_WITH_INITIALS]}

reg_no: E/{batch}/{regNo}
batch: E{batch}

department: {deparment}
current_affiliation: Department of Computer Engineering, University of Peradeniya

full_name: {studentData[FULL_NAME]}
name_with_initials: {studentData[NAME_WITH_INITIALS]}
preferred_short_name: {studentData[PREFERRED_SHORT_NAME]}
preferred_long_name: {studentData[PREFERRED_LONG_NAME]}
honorific: {studentData[HONORIFIC]}

email_faculty: {studentData[FACULTY_EMAIL]}
email_personal: {studentData[PERSONAL_EMAIL]}

location: {studentData[LOCATION]}

url_cv: {studentData[URL_CV]}
url_website: {studentData[URL_PERSONAL]}
url_linkedin: {studentData[URL_LINKEDIN]}
url_github: {studentData[URL_GITHUB]}
url_facebook: {studentData[URL_FB]}
url_researchgate: {studentData[URL_RESEARCHGATE]}
url_twitter: {studentData[URL_TWITTER]}

interests: {interests}

image_url: {image_path}
---"""

        # write to file
        htmlFile = open(
            "../"+f"pages/students/e{batch}/e{batch}{regNo}.html", "w")
        htmlFile.write(outputString)
        htmlFile.close()
