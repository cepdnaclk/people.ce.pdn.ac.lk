# Update student profile pictures using the data taken from Google Form
# Form URL - https://forms.gle/eor3v3nuf1752DGn7 Owned by: e18098@eng.pdn.ac.lk

# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk

import requests
import os
import gdown  # pip install gdown

googleFromCSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSFydisugm8TssaGPMhfqq0rS25mADtYUOxIlWc7cg_xvW8XRZAjl0d4G0I7DaC24939qepVBH-EzHX/pub?output=csv"
googleFromCSV = requests.get(googleFromCSV, headers={
                             'Cache-Control': 'no-cache'}).text.split("\n")

# Index of the CSV parameters
TIMESTAMP = 0
EMAIL = 1
REG_NO = 2
DEPARTMENT = 3
FULL_NAME = 4
NAME_WITH_INITIALS = 5
PREFERRED_SHORT_NAME = 6
PREFERRED_LONG_NAME = 7
HONORIFIC = 8
FACULTY_EMAIL = 9
PERSONAL_EMAIL = 10
LOCATION = 11
URL_CV = 12
URL_PERSONAL = 13
URL_LINKEDIN = 14
URL_GITHUB = 15
URL_FB = 16
URL_RESEARCHGATE = 17
URL_TWITTER = 18
INTERESTS = 19
URL_IMAGE = 20

if __name__ == "__main__":
    for eachLine in googleFromCSV:
        studentData = eachLine.split(",")

        if len(studentData) != 21:
            print("Splitted csv is longer than it should be!")
            quit()

        if ":" not in studentData[0]:
            # if there is no data in this line or this is the header line
            continue

        print("Processing: " + studentData[REG_NO])
        # get batch and regNo
        batch = studentData[REG_NO][2:4]  # 18
        regNo = studentData[REG_NO][5:].strip()  # 098

        permalink = f"/students/e{batch}/{regNo}"

        # get department
        deparment = ""
        if studentData[DEPARTMENT] == "Department of Computer Engineering":
            deparment = "Computer"
        elif studentData[DEPARTMENT] == "Department of Mechanical Engineering":
            deparment = "Mechanical"
        elif studentData[DEPARTMENT] == "Department of Manufacturing & Industrial Engineering":
            department = "Manufacturing"

        # interests
        interests = ",".join(studentData[INTERESTS].split(";"))
        # location
        location = ",".join(studentData[LOCATION].split(";"))

        # image
        image_path = f"images/students/e{batch}/e{batch}{regNo}.jpg"
        print(f"Downloading image to {image_path}")
        gdown.download("https://drive.google.com/uc?id=" +
                       studentData[URL_IMAGE].split("=")[1], "../"+image_path, quiet=True)

        # add # to all empty fields
        for i in range(0, URL_IMAGE+1):
            if studentData[i] == "":
                studentData[i] = "#"

        outputString = f"""---
layout: studentDetails
permalink: "/students/e{batch}/{regNo}/"
title: {studentData[NAME_WITH_INITIALS]}

reg_no: E/{batch}/{regNo}
batch: E{batch}

department: {deparment}
current_affiliation: {studentData[DEPARTMENT]}, University of Peradeniya

full_name: {studentData[FULL_NAME]}
name_with_initials: {studentData[NAME_WITH_INITIALS]}
preferred_short_name: {studentData[PREFERRED_SHORT_NAME]}
preferred_long_name: {studentData[PREFERRED_LONG_NAME]}
honorific: {studentData[HONORIFIC]}

email_faculty: {studentData[FACULTY_EMAIL]}
email_personal: {studentData[PERSONAL_EMAIL]}

location: {location}

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
