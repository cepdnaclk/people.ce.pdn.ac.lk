# Update student profile pictures using the data taken from Google Form
# Form URL - https://forms.gle/7EmpS2b84xxUENU67 Owned by: nuwanjaliyagoda@eng.pdn.ac.lk

# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk

# NOTES:
# Curently not considering the profile pages created batches before E14
# This differ form students from the fields department and current appiliation
# Alumini details may overwrite the details filled in the Student form

import requests
import os
import gdown  # pip install gdown
import student_profile_page_titles
import resize_student_images

googleFromCSV_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ6vtkNtEmxBOW3kAe_8OtJGF4Vcr-BglZgRYF2xvHDwXpLd1yUpzU4Wudxbi4G1WUYT3E-4sVhamjo/pub?output=csv"
googleFromCSV = requests.get(googleFromCSV_link, headers={
                             'Cache-Control': 'no-cache'}).text.split("\n")

# Index of the CSV parameters
TIMESTAMP = 0
EMAIL = 1
REG_NO = 2
FULL_NAME = 3
NAME_WITH_INITIALS = 4
PREFERRED_SHORT_NAME = 5
PREFERRED_LONG_NAME = 6
HONORIFIC = 7
FACULTY_EMAIL = 8
PERSONAL_EMAIL = 9
LOCATION = 10
CURRENT_AFFILIATION = 11  # new
URL_CV = 12
URL_PERSONAL = 13
URL_LINKEDIN = 14
URL_GITHUB = 15
URL_FB = 16
URL_TWITTER = 17
URL_RESEARCHGATE = 18
INTERESTS = 19
URL_IMAGE = 20

if __name__ == "__main__":
    for eachLine in googleFromCSV:
        studentData = eachLine.replace('\r', '').split(",")

        if len(studentData) != 21:
            print(
                f"Splitted csv is longer/shorter than it should be! {len(studentData)}")
            quit()

        if ":" not in studentData[0]:
            # if there is no data in this line or this is the header line
            continue

        # print(studentData)
        print("Processing: " + studentData[REG_NO])
        # get batch and regNo
        batch = studentData[REG_NO].split("/")[1].lower()  # 18 or 02A
        regNo = studentData[REG_NO].split("/")[2]  # 098

        permalink = f"/students/e{batch}/{regNo}"

        # set department
        deparment = "Computer Engineering"

        # interests
        interests = ",".join(studentData[INTERESTS].split(";"))

        # location
        location = ",".join(studentData[LOCATION].split(";"))

        # image
        image_path = f"images/students/e{batch}/e{batch}{regNo}.jpg"
        if studentData[URL_IMAGE] != "" and len(studentData[URL_IMAGE]) > 1:
            print(f"Downloading image to {image_path}")
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
title: {studentData[NAME_WITH_INITIALS]}

reg_no: E/{batch.upper()}/{regNo}
batch: E{batch.upper()}

department: {deparment}
current_affiliation: \"{studentData[CURRENT_AFFILIATION]}\"

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

interests: \"{interests}\"

image_url: {image_path}
---"""

        # write to file
        file_url = "../"+f"pages/students/e{batch}/e{batch}{regNo}.html"
        os.makedirs(os.path.dirname(file_url), exist_ok=True)
        htmlFile = open(file_url, "w")
        htmlFile.write(outputString)
        htmlFile.close()

        print("-------------")

print("Updating Student page titles")
student_profile_page_titles.run()
print("Resizing Images")
resize_student_images.run()
