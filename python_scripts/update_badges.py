# -------------------------------------------------------------------------------------------
# Update the badgers and assign to students
#
# Author: E/15/150 Nuwan Jaliyagoda - nuwanjaliyagoda@eng.pdn.ac.lk
# -------------------------------------------------------------------------------------------


import json
import os

import requests
import yaml
from util.helpers import delete_folder, get_student_profile, get_students_dict

# Constants
PAGES_DIR = "../pages/badges/pages/"
BADGES_JSON_PATH = "../_data/badges.json"


def create_badge_page(data, students):
    print(" ", data["title"])

    page_url = os.path.join(PAGES_DIR, f"{data['tag']}.md")
    gh_link = f"https://github.com/cepdnaclk/people.ce.pdn.ac.lk/blob/main/badges/{data['tag']}"

    student_list = []
    for s in data["students"]:
        student_enumber = s["eNumber"]
        if student_enumber in students:
            student = get_student_profile(students[student_enumber])
            print("\t", student_enumber, s["position"])
            student_list.append(
                {
                    "eNumber": student_enumber,
                    "name": student["name"],
                    "position": str(s["position"]),
                    "profile_url": student["profile_url"],
                    "profile_image": student["profile_image"],
                    "link": s["link"] if "link" in s else "#",
                }
            )

    page_content = {
        "layout": "badge_page",
        "title": data["title"],
        "subtitle": data["subtitle"],
        "permalink": f"/badges/{data['tag']}/",
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


def save_badges_json(badges_file):
    """Save the badges data to a JSON file."""
    os.makedirs(os.path.dirname(BADGES_JSON_PATH), exist_ok=True)
    with open(BADGES_JSON_PATH, "w") as f:
        f.write(json.dumps(badges_file, indent=4))


students = get_students_dict()

# Delete the existing pages first
delete_folder(PAGES_DIR)

path = "../badges/"
directory_list = os.listdir(path)
badges_file = {"badges": {}, "members": {}}

for filename in directory_list:
    print(">", filename)
    with open(path + filename, "r", encoding="utf-8") as file:
        badge_data = json.load(file)
        tag = badge_data["tag"]
        page_url = f"/badges/{tag}/"

        # Append badge details
        badges_file["badges"][tag] = {
            "title": badge_data["title"],
            "subtitle": badge_data["subtitle"],
            "image": badge_data["image"],
            "description": badge_data["description"],
            "page": page_url,
            "show": badge_data["show_in_profile"],
        }

        # Append student details
        for stud in badge_data["students"]:
            eNumber = stud.get("eNumber")

            if eNumber not in badges_file["members"]:
                badges_file["members"][eNumber] = []

            badges_file["members"][eNumber].append(
                {
                    "tag": tag,
                    "position": stud.get("position", ""),
                    "link": stud.get("link", "#"),
                }
            )

        # Create a page for the badge
        create_badge_page(badge_data, students)

# Sort badge list for each student
for stud in badges_file["members"]:
    badges_file["members"][stud] = sorted(
        badges_file["members"][stud], key=lambda item: item["tag"]
    )

save_badges_json(badges_file)
print("Badges updated successfully.")
