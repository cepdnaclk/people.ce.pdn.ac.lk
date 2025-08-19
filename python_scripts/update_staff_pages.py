import json
import os
import shutil
from datetime import datetime

import requests

DIRECTORY = "../_data/"
BASE_URL = "https://portal.ce.pdn.ac.lk/api/taxonomy/v1/term"

api_metadata = {
    "SUPPORT_STAFF": {
        "title": "Academic Support Staff",
        "description": "List of academic support staff members.",
        "source": f"{BASE_URL}/academic-support-staff",
        "last_updated": datetime.now().isoformat(),
    },
    "TEMPORARY_STAFF": {
        "title": "Temporary Academic Staff",
        "description": "List of temporary academic staff members.",
        "source": f"{BASE_URL}/temporary-academic-staff",
        "last_updated": datetime.now().isoformat(),
    },
}


def delete_folder(dir_path):
    """Delete the existing folder"""
    try:
        shutil.rmtree(dir_path)
    except FileNotFoundError:
        print(f"Error: Courses Folder Not Found at path: {dir_path}")


def get_staff_list(url):
    """Fetch the staff list from the given API URL."""
    response = requests.get(url, timeout=10)
    api_data = response.json()
    return api_data.get("data", []).get("terms", [])


def save_staff_list(staff_list, file_url: str, metadata: dict):
    """Saves the staff list to a JSON file."""
    # Sort the list by the 'joined_date' value
    staff_list.sort(key=lambda x: x.get("joined_date", ""))
    data = {
        "metadata": metadata,
        "data": staff_list,
    }

    # Save the data to a JSON file
    if not os.path.exists(os.path.dirname(file_url)):
        os.makedirs(os.path.dirname(file_url))
    with open(file_url, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def download_image(image_url, save_dir):
    """Download an image from a URL and save it to a local path."""
    # Download profile image and update the url_image path
    if image_url and image_url != "#":
        image_filename = f"/{save_dir}/{image_url.split('/')[-1]}"
        file_url = "../" + image_filename
        try:
            image_response = requests.get(image_url, timeout=10)
            if image_response.status_code == 200:
                os.makedirs(os.path.dirname(file_url), exist_ok=True)
                with open(file_url, "wb") as img_file:
                    img_file.write(image_response.content)
                return image_filename
        except requests.RequestException as e:
            print(f"Failed to download image for {s.get('name', 'unknown')}: {e}")


# ---------------------------------------------------------------------------
# Clean up existing staff folders
delete_folder("../images/staff/non-academic-staff")


# Fetch and save academic support staff list
support_staff_raw = get_staff_list(api_metadata["SUPPORT_STAFF"]["source"])
support_staff = []

for s in support_staff_raw:
    metadata = s.get("metadata", {})
    support_staff.append(
        {
            "staff_name": s.get("name", "").strip(),
            "text_below_name": metadata.get("designation", "-").strip(),
            "url_image": download_image(
                metadata.get("profile_image", "#").strip(),
                "images/staff/non-academic-staff",
            ),
            "contact_number": metadata.get("telephone", "").strip(),
            "email": metadata.get("email", "").strip(),
            "joined_date": metadata.get("joined_date", "").strip(),
            "left_date": metadata.get("leave_date", "").strip(),
        }
    )


file_url = f"{DIRECTORY}/non_academic_staff.json"
save_staff_list(support_staff, file_url, api_metadata["SUPPORT_STAFF"])

# ---------------------------------------------------------------------------
# Clean up existing staff folders
delete_folder("../images/staff/temporary-academic-staff")

# Fetch and save the temporary academic staff list
temporary_staff_raw = get_staff_list(api_metadata["TEMPORARY_STAFF"]["source"])
temporary_staff = []

for s in temporary_staff_raw:
    metadata = s.get("metadata", {})
    temporary_staff.append(
        {
            "staff_name": s.get("name", "").strip(),
            "text_below_name": metadata.get("designation", "-").strip(),
            "url_image": download_image(
                metadata.get("profile_image", "#").strip(),
                "images/staff/temporary-academic-staff",
            ),
            "email": metadata.get("email", "").strip(),
            # "url_profile": "#",
            "linkedin": metadata.get("url_linkedin", "#").strip(),
            "joined_date": metadata.get("joined_date", "").strip(),
            "left_date": metadata.get("leave_date", "").strip(),
        }
    )


file_url = f"{DIRECTORY}/temporary_academic_staff.json"
save_staff_list(temporary_staff, file_url, api_metadata["TEMPORARY_STAFF"])
