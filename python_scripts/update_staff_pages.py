# -------------------------------------------------------------------------------------------
# Update the staff pages by fetching data from the Taxonomy APIs and saving it to JSON files.
# Also downloads and saves profile images locally.

# Author: E/15/150 Nuwan Jaliyagoda - nuwanjaliyagoda@eng.pdn.ac.lk
# -------------------------------------------------------------------------------------------

import json
import os
import re

import requests
import yaml
from util.helpers import delete_folder, download_image, get_taxonomy_page

DIRECTORY = "../_data/"
BASE_URL = "https://portal.ce.pdn.ac.lk/api/taxonomy/v1/term"

api_metadata = {
    "ACADEMIC_STAFF": {
        "title": "Academic Staff",
        "description": "List of academic staff members.",
        "source": f"{BASE_URL}/academic-staff",
        # "last_updated": datetime.now().isoformat(),
    },
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
        response = requests.get(url, timeout=30)
        api_data = response.json()
        return api_data.get("data", {}).get("terms", [])
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


def save_academic_staff_page(details: dict, file_url: str):
    page_url = details.pop("page")
    page_content = get_taxonomy_page(page_url) if page_url and page_url != "#" else ""
    try:
        # Save the data to a HTML file with jekyll front matter
        if not os.path.exists(os.path.dirname(file_url)):
            os.makedirs(os.path.dirname(file_url))
        with open(file_url, "w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(yaml.dump(details, sort_keys=False))
            f.write("---\n\n")
            f.write("\n")
            f.write(
                "<!-- This is automatically updated from portal.ce.pdn.ac.lk content -->"
            )
            f.write("\n")
            f.write(page_content)
            f.write("\n")
    except IOError as e:
        print(f"Failed to save staff page to {file_url}: {e}")


# ---------------------------------------------------------------------------

# Clean up existing academic staff folders
delete_folder("../images/staff/academic-staff")
delete_folder("../pages/staff/academic-staff")

print("\n>> Fetching and saving academic staff list...")

# Fetch and save support staff list
academic_staff_raw = get_staff_list(api_metadata["ACADEMIC_STAFF"]["source"])
academic_staff = []

for role in academic_staff_raw:
    for s in role.get("terms", []):
        print(role["name"], ">", s["name"])
        metadata = s.get("metadata", {})

        # TODO Update the keys in staff pages to match new configs
        data = {
            "layout": "staffDetails",
            "permalink": f"/staff/academic/{s.get('code', '').strip()}",
            "title": s.get("name", "").strip(),
            "name_below_image": metadata.get("designation", "").strip(),
            "contact_number": metadata.get("telephone", "").strip(),
            "email": metadata.get("email", "").strip(),
            "location": metadata.get("location", "-").strip(),
            "text_below_name": metadata.get("designation", "").strip(),
            "url_image": download_image(
                metadata.get("profile_image", "#").strip(),
                "images/staff/academic-staff",
            ),
            "url_website": metadata.get("website", "#").strip(),
            "url_google_scholar": metadata.get("url_google_scholar", "#").strip(),
            "url_researchgate": metadata.get("url_researchgate", "#").strip(),
            "url_linkedin": metadata.get("url_linkedin", "#").strip(),
            "url_orcid": metadata.get("url_orcid", "#").strip(),
            "url_ad_scientific_index": metadata.get(
                "url_ad_scientific_index", "#"
            ).strip(),
            "designation": metadata.get("designation", "").strip(),
            "is_hod": metadata.get("is_hod", False),
            "on_duty": metadata.get("on_duty", False),
            "research_interests": [
                re.sub(r"^['\"]|['\"]$", "", interest.strip())
                for interest in metadata.get("research_interests", "").split(",")
                if interest.strip()
            ],
            "page": metadata.get("profile_content", "").strip(),
        }
        academic_staff.append(data)

        file_url = f"../pages/staff/academic-staff/{s.get('code', '').strip()}.html"
        save_academic_staff_page(data, file_url)

# ---------------------------------------------------------------------------

# Clean up existing support staff folders
delete_folder("../images/staff/non-academic-staff")

print("\n>> Fetching and saving academic support staff list...")

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
# Clean up existing temporary staff folders
delete_folder("../images/staff/temporary-academic-staff")

print("\n>> Fetching and saving temporary academic staff list...")

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
