# Update student/alumni profile pictures using the data taken from Google Form
# Form URL - https://forms.gle/Q4LfzATdAF8AXTCA8 Owned by: nuwanjaliyagoda@eng.pdn.ac.lk
# This uses the latest unified google form

# Authors:
# E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk
# E/15/140 Nuwan Jaliyagoda - nuwanjaliyagoda@eng.pdn.ac.lk

import json
import os
import subprocess
from datetime import datetime
from os.path import exists

import gdown
import requests
import student_profile_page_titles
from PIL import Image
from pytz import timezone

# run export GOOGLE_FORM_CSV_LINK="url" to set environment variables
# file can be found in the drive folder
# instructions to run the file can be found in the script
googleFormCSV_link = os.environ["GOOGLE_FORM_CSV_LINK"]
googleFormCSV = requests.get(
    googleFormCSV_link, headers={"Cache-Control": "no-cache"}
).text.split("\n")

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
    for eachLine in googleFormCSV:
        studentData = eachLine.replace("\r", "").split(",")
        if len(studentData) != 23:
            print(
                f"WARNING! Splitted csv is longer/shorter than it should be! {len(studentData)}"
            )
            quit()

        if ":" not in studentData[TIMESTAMP]:
            # if there is no timestamp in this line or this is the header line
            continue

        # If timestamp is older than 10 days, skip the record
        if (
            datetime.now(timezone("Asia/Colombo"))
            - datetime.strptime(
                studentData[TIMESTAMP] + " +05:30", "%m/%d/%Y %H:%M:%S %z"
            )
        ).days > 2:
            continue

        print("Processing: " + studentData[REG_NO] + " " + studentData[FULL_NAME])

        # Get batch and regNo
        batch = studentData[REG_NO].split("/")[1].lower()  # Ex: 18 or 02A
        regNo = studentData[REG_NO].split("/")[2]  # Ex: 098

        permalink = f"/students/e{batch}/{regNo}"

        # set department and current affiliation if student
        if studentData[STUDENT_OR_ALUMNI] == "An past student / alumni":
            department = "Computer Engineering"

        elif studentData[DEPARTMENT] == "Department of Computer Engineering":
            # if student, google form doesn't take current affiliation
            studentData[CURRENT_AFFILIATION] = "Department of Computer Engineering"
            department = "Computer Engineering"

        elif studentData[DEPARTMENT] == "Department of Mechanical Engineering":
            # if student, google form doesn't take current affiliation
            studentData[CURRENT_AFFILIATION] = "Department of Mechanical Engineering"
            department = "Mechanical Engineering"
        else:
            # Default option
            department = "Computer Engineering"

        # interests
        interests = ",".join(studentData[INTERESTS].split(";"))

        # location
        location = ",".join(studentData[LOCATION].split(";"))

        # check if the file was updated using pull requests after the form was filed
        file_url = "../" + f"pages/students/e{batch}/e{batch}{regNo}.html"

        existing_content_after_frontmatter = ""

        if exists(file_url):
            # TODO: Read the content after the frontmatter, and keep it to avoid overridden by Google Form data
            with open(file_url, encoding="utf-8") as existingFile:
                three_dash_count = 0
                for eachLine in existingFile:
                    if three_dash_count != 2:
                        if eachLine == "---\n":
                            three_dash_count += 1
                    else:
                        existing_content_after_frontmatter += eachLine

            # Get last modified time from git log
            file_last_edited_date_str = str(
                subprocess.run(
                    ["git", "log", "-1", '--pretty="format:%ci"', file_url],
                    stdout=subprocess.PIPE,
                ).stdout
            )
            first_index = file_last_edited_date_str.find(":") + 1
            last_index = file_last_edited_date_str.find('"', first_index)
            file_last_edited_date_str = file_last_edited_date_str[
                first_index:last_index
            ]
            file_last_edited_date = datetime.strptime(
                file_last_edited_date_str, "%Y-%m-%d %H:%M:%S %z"
            )
            google_form_filled_date = datetime.strptime(
                studentData[TIMESTAMP] + " +05:30", "%m/%d/%Y %H:%M:%S %z"
            )
            print(
                f"file_last_edited_date: {file_last_edited_date}, google_form_filled_date: {google_form_filled_date}, Difference: {(file_last_edited_date - google_form_filled_date).total_seconds()}"
            )

            # if (file_last_edited_date - google_form_filled_date).total_seconds() > 0:
            #     print("File was updated after the google form was filled. Skipping...")
            #     print("-------------")
            #     continue

        # image
        image_base = f"images/students/e{batch}/e{batch}{regNo}"

        # default, updated after detecting actual format
        image_path = f"{image_base}.jpg"

        # Create folder if not exists
        os.makedirs(os.path.dirname("../" + image_path), exist_ok=True)

        is_image_downloaded = False  # used to create the json file for alumni
        if studentData[URL_IMAGE] != "" and len(studentData[URL_IMAGE]) > 1:
            print(f"Downloading image for {studentData[REG_NO]}")
            # print(len(studentData[URL_IMAGE]))
            try:
                tempImageName = "image.temp"
                gdown.download(
                    "https://drive.google.com/uc?id="
                    + studentData[URL_IMAGE].split("=")[1].strip(),
                    "./" + tempImageName,
                    quiet=True,
                )
                image = Image.open(tempImageName)
                format_to_ext = {
                    "JPEG": "jpg",
                    "PNG": "png",
                    "GIF": "gif",
                    "WEBP": "webp",
                    "BMP": "bmp",
                }
                ext = format_to_ext.get(image.format, "jpg")
                image_path = f"{image_base}.{ext}"
                print(f"Saving image as {image_path} (format: {image.format})")
                image.save("../" + image_path)
                is_image_downloaded = True
                os.system("rm '" + tempImageName + "'")

                # alternative to gdown
                # os.system(
                #     f"wget https://drive.google.com/uc?id={studentData[URL_IMAGE].split('=')[1].strip()} -O ../{image_path}")
            except:
                print("WARNING! Image download failed !")

        else:
            print("Image not specified")

        # add # to all empty fields
        for i in range(0, URL_IMAGE + 1):
            if studentData[i] == "":
                studentData[i] = "#"

        outputString = f"""---
layout: studentDetails
permalink: "/students/e{batch.lower()}/{regNo}/"
title: {studentData[NAME_WITH_INITIALS].title()}

reg_no: E/{batch.upper()}/{regNo}
batch: E{batch.upper()}

department: \"{department}\"
current_affiliation: \"{studentData[CURRENT_AFFILIATION]}\"

full_name: {studentData[FULL_NAME].title()}
name_with_initials: {studentData[NAME_WITH_INITIALS].title()}
preferred_short_name: {studentData[PREFERRED_SHORT_NAME].title()}
preferred_long_name: {studentData[PREFERRED_LONG_NAME].title()}
honorific: {studentData[HONORIFIC]}

email_faculty: {studentData[FACULTY_EMAIL]}
email_personal: {studentData[PERSONAL_EMAIL]}

location: \"{location}\"

url_cv: {studentData[URL_CV]}
url_website: {studentData[URL_PERSONAL]}
url_linkedin: {studentData[URL_LINKEDIN]}
url_github: {studentData[URL_GITHUB]}
url_facebook: {studentData[URL_FB]}
url_researchgate: {studentData[URL_RESEARCHGATE]}
url_twitter: {studentData[URL_TWITTER]}

interests: \"{interests}\"

image_url: {image_path}
---

"""

        os.makedirs(os.path.dirname(file_url), exist_ok=True)
        with open(file_url, "w", encoding="utf-8") as htmlFile:
            htmlFile.write(outputString + existing_content_after_frontmatter)

        # update json if below E14
        if (int(batch[0:2]) < 14) or int(batch[0:2]) == 99 or int(batch[0:2]) == 98:
            print("Updating JSON in _data folder")

            # select student from json file
            json_path = f"../_data/stud/e{batch.lower()}.json"
            with open(json_path, encoding="utf-8") as f:
                dataInJSON = json.load(f)
            try:
                thisStudent = dataInJSON[studentData[REG_NO].upper()]
            except KeyError as e:
                print(
                    "Student doesn't exist in the json files. Creating new entry",
                    "*" * 20,
                )
                dataInJSON[studentData[REG_NO].upper()] = {}
                thisStudent = dataInJSON[studentData[REG_NO].upper()]
                thisStudent["reg_no"] = studentData[REG_NO].upper()

                # reorder the dict
                dataInJSON = dict(sorted(dataInJSON.items()))

            # change data
            thisStudent["page_url"] = f"/students/e{batch.lower()}/{regNo}/"
            thisStudent["name_with_initials"] = f"{studentData[NAME_WITH_INITIALS]}"
            if is_image_downloaded:
                thisStudent["image_url"] = image_path

            # write data back into json file
            with open(json_path, "w", encoding="utf-8") as jsonFile:
                jsonFile.write(json.dumps(dataInJSON, indent=2))

        print("-------------")

print("\n\n\n\n")
print("Updating Student page titles")
student_profile_page_titles.run()
