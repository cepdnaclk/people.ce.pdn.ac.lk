# -------------------------------------------------------------------------------------------
# Update the staff pages by fetching data from the Taxonomy APIs and saving it to JSON files.
# Also downloads and saves profile images locally.

# Author: E/15/150 Nuwan Jaliyagoda - nuwanjaliyagoda@eng.pdn.ac.lk
# -------------------------------------------------------------------------------------------

import json
import os

import requests
from util.helpers import delete_folder, download_image

DIRECTORY = "../_data/"
BASE_URL = "https://portal.ce.pdn.ac.lk/api/taxonomy/v1/term"

api_metadata = {
    "SUPPORT_STAFF": {
        "title": "Academic Support Staff",
        "description": "List of academic support staff members.",
        "source": f"{BASE_URL}/academic-support-staff",
        # "last_updated": datetime.now().isoformat(),
    },
    "TEMPORARY_STAFF": {
        "title": "Temporary Academic Staff",
        "description": "List of temporary academic staff members.",
        "source": f"{BASE_URL}/temporary-academic-staff",
        # "last_updated": datetime.now().isoformat(),
    },
}


def get_staff_list(url):
    """Fetch the staff list from the given API URL."""
    try:
        response = requests.get(url, timeout=10)
        api_data = response.json()
        return api_data.get("data", []).get("terms", [])
    except requests.RequestException as e:
        print(f"Failed to fetch staff list from {url}: {e}")
        return []
    except ValueError as e:
        print(f"Failed to parse JSON response from {url}: {e}")
        return []


def save_staff_list(staff_list, file_url: str, metadata: dict):
    """Saves the staff list to a JSON file."""
    # Sort the list by the 'joined_date' value
    staff_list.sort(key=lambda x: x.get("joined_date", ""))
    data = {
        "metadata": metadata,
        "data": staff_list,
    }

    try:
        # Save the data to a JSON file
        if not os.path.exists(os.path.dirname(file_url)):
            os.makedirs(os.path.dirname(file_url))
        with open(file_url, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Failed to save staff list to {file_url}: {e}")


# ---------------------------------------------------------------------------

# Clean up existing staff folders
delete_folder("../images/staff/non-academic-staff")

print(">> Fetching and saving academic support staff list...")

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

print(">> Fetching and saving temporary academic staff list...")

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
