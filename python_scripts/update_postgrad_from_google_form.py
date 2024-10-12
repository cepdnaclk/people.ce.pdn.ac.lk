# Update postgraduate student details using the data taken from Google Form
# Form URL - https://forms.gle/mpo2jarU7b9eWz9F7
# Issue 138 - https://github.com/cepdnaclk/people.ce.pdn.ac.lk/issues/138

# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk


import requests
import os
import gdown  # pip install gdown
import datetime
import shutil
import json
import csv

googleFromCSV_link = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR6ntuDUUuzQS84Am7NMcCc6LCTYKmUfMbVhp4dvy1AXWoVxNrjWfeQntWg5cAfLsFvb4WASQRp-erT/pub?output=csv"
googleFromCSV = requests.get(
    googleFromCSV_link, headers={"Cache-Control": "no-cache"}
).text.split("\n")

# Index of the CSV parameters
FORM_FILLED_DATE = 0
EMAIL = 1
REG_NO = 2
NAME_WITH_INITIALS = 5
DEGREE = 8
MODE_OF_STUDY = 9
RESEARCH_TOPIC = 11
YEAR_OF_COMPLETION = 12
PROFILE_PIC_LINK = 15
WEBSITE_URL = 16


i = 0
if __name__ == "__main__":
    try:
        # shutil.rmtree('../images/students/postgraduate/')
        shutil.rmtree("../pages/postgraudate/students")
    except OSError as e:
        print("Error: %s : %s" % ("Directory remove failed", e.strerror))

    csv_reader = csv.reader(googleFromCSV, delimiter=",")
    for eachLine in csv_reader:
        studentData = eachLine

        if ":" not in studentData[0]:
            # if there is no timestamp in this line or this is the header line
            continue

        # calcualte a number from the time the form is filled
        # based on the time elapsed from the start of time (1970 something)
        parsedDateTimeObject = datetime.datetime.strptime(
            studentData[FORM_FILLED_DATE], "%m/%d/%Y %H:%M:%S"
        )
        elapsedTimeFromTheStartOfTime = parsedDateTimeObject.timestamp() - 1654224090
        print(int(elapsedTimeFromTheStartOfTime))

        # print(studentData)
        print(
            "Processing: " + studentData[REG_NO] + " " + studentData[NAME_WITH_INITIALS]
        )

        print(json.dumps(studentData, indent=4))

        nameConverted = (
            studentData[NAME_WITH_INITIALS].replace(" ", "").replace(".", "")
        )
        permalink = f"/students/postgraduate/{nameConverted}/"

        # image
        image_path = f"images/students/postgraduate/{nameConverted}.jpg"
        os.makedirs(os.path.dirname(image_path), exist_ok=True)

        isImageDownloaded = False
        if (
            studentData[PROFILE_PIC_LINK] != ""
            and len(studentData[PROFILE_PIC_LINK]) > 1
        ):
            if not os.path.exists("../" + image_path):
                print(f"Downloading image to {image_path}")
                isImageDownloaded = True
                # print(studentData[PROFILE_PIC_LINK])
                gdown.download(
                    "https://drive.google.com/uc?id="
                    + studentData[PROFILE_PIC_LINK].split("=")[1].strip(),
                    "../" + image_path,
                    quiet=True,
                )
            else:
                print("Profile pic is already there")
        else:
            image_path = "images/students/default.jpg"
            print("Image not specified")

        # add # to all empty fields
        for i in range(0, WEBSITE_URL + 1):
            if studentData[i] == "":
                studentData[i] = "#"

        reg_number = studentData[REG_NO]
        if reg_number.lower() == "provisional":
            # Some will not type it in the correct case
            reg_number = "Provisional"

        outputString = f"""---
layout: postgraduateDetails
permalink: "{permalink}"
title: {studentData[NAME_WITH_INITIALS]}
index_in_card_list: {int(elapsedTimeFromTheStartOfTime)}

reg_no: {reg_number}
name_with_initials: {studentData[NAME_WITH_INITIALS]}
email: {studentData[EMAIL]}
url_website: {studentData[WEBSITE_URL]}
degree: {studentData[DEGREE]}
mode_of_study: {studentData[MODE_OF_STUDY]}
research_topic: {studentData[RESEARCH_TOPIC]}

image_url: "{image_path}"
---"""

        # write to html file
        file_url = "../" + f"pages/postgraudate/students/{nameConverted}.html"
        os.makedirs(os.path.dirname(file_url), exist_ok=True)
        htmlFile = open(file_url, "w")
        print(f"Writing to {file_url}")
        htmlFile.write(outputString)
        htmlFile.close()

print("Done")
