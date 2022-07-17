# Update student/alumni profile pictures using the data taken from Google Form
# Form URL - https://forms.gle/Q4LfzATdAF8AXTCA8 Owned by: nuwanjaliyagoda@eng.pdn.ac.lk
# This uses the latest unified google form

# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk


import requests
import os
import gdown  # pip install gdown
import json  # to edit _data/exx.json
import student_profile_page_titles

googleFromCSV_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTZRR_UqRS_MHtl8Hlyv92dbgRJb342zguSm0DOdcpiYA5k7b2RceNmjBBKCu5AcX4A9RxQXazzWIEx/pub?output=csv"
googleFromCSV = requests.get(googleFromCSV_link, headers={
                             'Cache-Control': 'no-cache'}).text.split("\n")

# Index of the CSV parameters
TIMESTAMP = 0
EMAIL = 1
REG_NO = 2
STUDENT_OR_ALUMNI = 3
DEPARTMENT = 4
CURRENT_AFFILIATION = 5
FULL_NAME = 6
NAME_WITH_INITIALS = 7
PREFERRED_SHORT_NAME = 8
PREFERRED_LONG_NAME = 9
HONORIFIC = 10
FACULTY_EMAIL = 11
PERSONAL_EMAIL = 12
LOCATION = 13
INTERESTS = 14
URL_IMAGE = 15
URL_CV = 16
URL_PERSONAL = 17
URL_LINKEDIN = 18
URL_GITHUB = 19
URL_FB = 20
URL_TWITTER = 21
URL_RESEARCHGATE = 22

i = 0
if __name__ == "__main__":
    for eachLine in googleFromCSV:
        studentData = eachLine.replace('\r', '').split(",")
        if len(studentData) != 23:
            print(f"Splitted csv is longer/shorter than it should be! {len(studentData)}")
            quit()

        if ":" not in studentData[0]:
            # if there is no timestamp in this line or this is the header line
            continue

        # print(studentData)
        print("Processing: " + studentData[REG_NO] + " " + studentData[FULL_NAME])
        # get batch and regNo
        batch = studentData[REG_NO].split("/")[1].lower()  # 18 or 02A
        regNo = studentData[REG_NO].split("/")[2]  # 098

        permalink = f"/students/e{batch}/{regNo}"

        # set department and curent affiliation if student
        if (studentData[STUDENT_OR_ALUMNI] == "An past student / alumni"):
            deparment = "Computer Engineering"
        elif (studentData[DEPARTMENT] == "Department of Computer Engineering"):
            # if student, google form doesnt take current affiliation
            studentData[CURRENT_AFFILIATION] = "Department of Computer Engineering"
            department = "Computer Engineering"
        elif (studentData[DEPARTMENT] == "Department of Mechanical Engineering"):
            # if student, google form doesnt take current affiliation
            print("This is a mechanical engineering student")
            studentData[CURRENT_AFFILIATION] = "Department of Mechanical Engineering"
            department = "Mechanical Engineering"

        # interests
        interests = ",".join(studentData[INTERESTS].split(";"))

        # location
        location = ",".join(studentData[LOCATION].split(";"))

        # image
        image_path = f"images/students/e{batch}/e{batch}{regNo}.jpg"
        isImageDownloaded = False
        if studentData[URL_IMAGE] != "" and len(studentData[URL_IMAGE]) > 1:
            print(f"Downloading image to {image_path}")
            isImageDownloaded = True
            # print(len(studentData[URL_IMAGE]))
            gdown.download("https://drive.google.com/uc?id=" +
                           studentData[URL_IMAGE].split("=")[1].strip(), "../"+image_path, quiet=True)
            # os.system(
            #     f"wget https://drive.google.com/uc?id={studentData[URL_IMAGE].split('=')[1].strip()} -O ../{image_path}")
        else:
            print("Image not specified")

        # add # to all empty fields
        for i in range(0, URL_IMAGE+1):
            if studentData[i] == "":
                studentData[i] = "#"

        outputString = f"""---
layout: studentDetails
permalink: "/students/e{batch.lower()}/{regNo}/"
title: {studentData[NAME_WITH_INITIALS].title()}

reg_no: E/{batch.upper()}/{regNo}
batch: E{batch.upper()}

department: {deparment}
current_affiliation: \"{studentData[CURRENT_AFFILIATION]}\"

full_name: {studentData[FULL_NAME].title()}
name_with_initials: {studentData[NAME_WITH_INITIALS].title()}
preferred_short_name: {studentData[PREFERRED_SHORT_NAME].title()}
preferred_long_name: {studentData[PREFERRED_LONG_NAME].title()}
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

interests: \"{interests}\"

image_url: {image_path}
---"""

        # write to html file
        file_url = "../"+f"pages/students/e{batch}/e{batch}{regNo}.html"
        os.makedirs(os.path.dirname(file_url), exist_ok=True)
        htmlFile = open(file_url, "w")
        htmlFile.write(outputString)
        htmlFile.close()

        # update json if below E14
        if (int(batch[0:2]) < 14) or int(batch[0:2]) == 99 or int(batch[0:2]) == 98:
            print("Updating JSON in _data folder")

            # select student from json file
            jsonPath = f"../_data/stud/e{batch.lower()}.json"
            dataInJSON = json.load(open(jsonPath))
            thisStudent = dataInJSON[studentData[REG_NO].upper()]

            # change data
            thisStudent["page_url"] = f"/students/e{batch.lower()}/{regNo}/"
            thisStudent["name_with_initials"] = f"{studentData[NAME_WITH_INITIALS]}"
            if isImageDownloaded:
                thisStudent["image_url"] = image_path

            # write data back into json file
            jsonFile = open(jsonPath, "w")
            jsonFile.write(json.dumps(dataInJSON, indent=4))

        print("-------------")

print("\n\n\n\n")
print("Updating Student page titles")
student_profile_page_titles.run()
print("Resizing Images")
