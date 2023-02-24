import requests
import os
import json
import shutil

# Where the data is available
studentSource = 'https://api.ce.pdn.ac.lk/people/v1/students/all/'

def getStud_profile(data):
    # TODO: Check the name options
    if(data['name_with_initials'] != ""):
        name = data["name_with_initials"]
    elif(data['preferred_long_name'] != ""):
        name = data["preferred_long_name"]
    elif(data['full_name'] != ""):
        name = data["full_name"]
    else:
        # Name not found
        return {}

    # if (data["honorific"] != ""):
    #     name = data["honorific"] + " " + name

    profile_img = "/assets/images/profile_default.jpg" if (data["profile_image"] == "") else data["profile_image"]
    profile_url = data["profile_page"].replace("https://people.ce.pdn.ac.lk", "")

    return {
        "name": name,
        "affiliation": data["current_affiliation"],
        "profile_url": profile_url,
        "profile_image": profile_img
    }

def create_page(data):
    # print(_data)

    page_url = '../pages/societies/pages/{0}.md'.format(data['tag'])
    gh_link = "https://github.com/cepdnaclk/people.ce.pdn.ac.lk/blob/main/societies/" + data['tag']

    os.makedirs(os.path.dirname(page_url), exist_ok=True)

    student_list = ""
    print('\n' + data['title'])

    for s in data['students']:
        student_eNumber = s['eNumber']

        if student_eNumber in students:
            print(student_eNumber, s['position'])
            student = getStud_profile(students[student_eNumber])
            if ('link' in s):
                link = s['link'] or "#"
            else:
                link = "#"

            student_list += "\n - { eNumber: \""+ student_eNumber + "\", name: \""+ student['name'] +"\", position: \"" + s['position'] + "\", profile_url: \"" + student['profile_url'] +"\", profile_image: \"" + student['profile_image'] +"\", link: \"" + link +"\" }"

        else:
            if(student_eNumber == ""):
                profile_image = "https://people.ce.pdn.ac.lk/images/students/default.jpg"
            else:
                batch = student_eNumber.split('/')[1].lower()
                profile_image = "https://people.ce.pdn.ac.lk/images/students/e{0}/{1}.jpg".format(batch, student_eNumber.replace("/","").lower())

            student_list += "\n - { eNumber: \""+ student_eNumber + "\", name: \""+ s['name'] +"\", position: \"" + s['position'] + "\", profile_url: \"#\", profile_image: \"" + profile_image +"\", link: \"\" }"

    page_content = """---
layout: society_page
title: """ + data['title'] + """
permalink: \"/societies/""" + data['tag'] + "/" + """\"
badge_image: \"""" + data['image'] + """\"
badge_description: \"""" + data['description'] + """\"
badge_criteria: \"""" + data['criteria'] + """\"
edit: \"""" + gh_link + """\"
students: """ + student_list + """
---
"""

    with open(page_url, "w") as f:
        f.write(page_content)


# All student details
r = requests.get(studentSource)

# Fetch data from the people.ce.pdn.ac.lk
if r.status_code == 200:
    students = json.loads(r.text)

# Delete the existing pages first
dir_path = "../pages/societies/pages/"
try:
    shutil.rmtree(dir_path)
except:
    print("Error: Folder Not Found!")

# Read the /batch folder and generate the file, _data/societies.json
path = "../societies/"
directory_list = os.listdir(path)

societies_file = { "committee": {}, "members": {}}

for filename in directory_list:
    print("\n-----------\n" + filename)
    society_data = json.load(open(path + filename, "r"))

    tag = society_data['tag']
    page_url = "/societies/{0}/".format(tag)

    # Append the badge details
    societies_file['committee'][tag] = {
        "title": society_data['title'],
        "image": society_data['image'],
        "description": society_data['description'],
        "page": page_url,
        "show": society_data['show_in_profile']
    }

    # Append the student details
    for stud in society_data['students']:
        eNumber = stud['eNumber']
        position = stud['position']

        if ('link' in stud):
            link = stud['link']  # Link to the certificate
        else:
            link = "#"

        if eNumber not in societies_file['members']: societies_file['members'][eNumber] = []
        societies_file['members'][eNumber].append({"tag": tag, "position": position, "link": link})

    # Create a page for the badge
    create_page(society_data)

# Generate the '_data/socities.json'
filename = "../_data/socities.json"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as f:
    f.write(json.dumps(societies_file, indent = 4))
