# -------------------------------------------------------------------------------------------
# Update the societies pages by reading data from the /societies folder, transform,
# and saving it into JSON files.
#
# Author: E/15/150 Nuwan Jaliyagoda - nuwanjaliyagoda@eng.pdn.ac.lk
# -------------------------------------------------------------------------------------------

import json
import os

import requests
import yaml
from util.helpers import delete_folder

# Where the data is available
BASE_URL = "https://api.ce.pdn.ac.lk/people/v1/students/all/"


def get_student_profile(data):
    """Fetch the student profile details from the people.ce.pdn.ac.lk data."""
    name = ""
    if data["name_with_initials"] != "":
        name = data["name_with_initials"]
    elif data["preferred_long_name"] != "":
        name = data["preferred_long_name"]
    elif data["full_name"] != "":
        name = data["full_name"]
    else:
        # Name not found
        return {}

    profile_img = (
        "/assets/images/profile_default.jpg"
        if (data["profile_image"] == "")
        else data["profile_image"]
    )
    profile_url = data["profile_page"].replace("https://people.ce.pdn.ac.lk", "")

    return {
        "name": name,
        "eNumber": data["eNumber"],
        "affiliation": data["current_affiliation"],
        "profile_url": profile_url,
        "profile_image": profile_img,
    }


def get_students_dict(url=BASE_URL):
    # All student details
    try:
        response = requests.get(url, timeout=10)
        api_data = response.json()
        return api_data
    except requests.RequestException as e:
        print(f"Failed to fetch students list from {url}: {e}")
        return []
    except ValueError as e:
        print(f"Failed to parse JSON response from {url}: {e}")
        return {}


def create_society_page(data, students):
    print(" ", data["title"])

    page_url = "../pages/societies/pages/{0}.md".format(data["tag"])
    gh_link = (
        "https://github.com/cepdnaclk/people.ce.pdn.ac.lk/blob/main/societies/"
        + data["tag"]
    )
    student_list = []

    for s in data["students"]:
        student_enumber = s["eNumber"]

        if student_enumber in students:
            student_data = get_student_profile(students[student_enumber])
            print("\t", student_enumber, s["position"])
            student_list.append(
                {
                    "eNumber": student_data["eNumber"],
                    "name": student_data["name"],
                    "position": s["position"],
                    "profile_url": student_data["profile_url"],
                    "profile_image": student_data["profile_image"],
                    "link": s["link"] if "link" in s else "#",
                }
            )

    page_content = {
        "layout": "society_page",
        "title": data["title"],
        "permalink": "/societies/{0}/".format(data["tag"]),
        "badge_image": data["image"],
        "badge_description": data["description"],
        "badge_criteria": data["criteria"],
        "edit": gh_link,
        "students": student_list,
    }

    os.makedirs(os.path.dirname(page_url), exist_ok=True)
    with open(page_url, "w") as f:
        f.write("---\n")
        yaml.dump(page_content, f, sort_keys=False)
        f.write("---\n")


students = get_students_dict()

# Delete the existing pages first
delete_folder("../pages/societies/pages/")


# Read the /societies folder and generate the file, _data/societies.json
path = "../societies/"
directory_list = os.listdir(path)
societies_file = {"committee": {}, "members": {}}

for filename in directory_list:
    print(">", filename)
    with open(path + filename, "r", encoding="utf-8") as file:
        society_data = json.load(file)
        society_tag = society_data["tag"]
        page_url = f"/societies/{society_tag}/"

        # Append the badge details
        societies_file["committee"][society_tag] = {
            "title": society_data["title"],
            "image": society_data["image"],
            "description": society_data["description"],
            "page": page_url,
            "show": society_data["show_in_profile"],
        }

        # Append the student details
        for student in society_data["students"]:
            eNumber = student["eNumber"]

            if eNumber not in societies_file["members"]:
                societies_file["members"][eNumber] = []

            societies_file["members"][eNumber].append(
                {
                    "tag": society_tag,
                    "position": student.get("position", ""),
                    "link": student.get("link", "#"),
                }
            )

        # Create a page for the badge
        create_society_page(society_data, students)

# Generate the '_data/societies.json'
FILENAME = "../_data/societies.json"
os.makedirs(os.path.dirname(FILENAME), exist_ok=True)
with open(FILENAME, "w") as f:
    f.write(json.dumps(societies_file, indent=2))
