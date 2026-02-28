# -------------------------------------------------------------------------------------------
# Gets the list of visiting research fellows by fetching data from the CE Portal API and saves it in the JSON file: 'visiting-research-fellows.json"

# Author: E/22/151 Imaadh Ifthikar - e22151@eng.pdn.ac.lk
# -------------------------------------------------------------------------------------------

import json
import os
#import re

import requests
#import yaml
from util.helpers import (
    #get_taxonomy_page_content,
    delete_folder,
    download_image,
)

DIRECTORY = "../_data"
BASE_URL = "https://portal.ce.pdn.ac.lk/api/taxonomy/v2/cepdnaclk/visiting-research-fellows"

api_metadata = {
    "VISITING_RESEARCH_FELLOWS": {
        "title": "Visiting Research Fellows",
        "description": "List of visiting research fellows.",
        "source": f"{BASE_URL}",
        # "last_updated": datetime.now().isoformat(),
    }
}

def get_fellows_list(url):
    """Fetch the visiting fellows' list from the given API URL."""
    try:
        response = requests.get(url, timeout=30)
        api_data = response.json()
        return api_data.get("data", {}).get("terms", [])
    except requests.RequestException as e:
        print(f"Failed to fetch visiting research fellows' list from {url}: {e}")
        return []
    except ValueError as e:
        print(f"Failed to parse JSON response from {url}: {e}")
        return []

def save_fellows_list(fellows_list, file_url: str, metadata: dict):
    """Saves the visiting research fellows' list to a JSON file."""
    # Sort the list by the 'name' value alphabetically
    fellows_list.sort(key=lambda x: x.get("name", ""))
    data = {
        "metadata": metadata,
        "data": fellows_list
    }

    try:
        # Save the data to a JSON file
        if not os.path.exists(os.path.dirname(file_url)):
            os.makedirs(os.path.dirname(file_url))
        with open(file_url, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Failed to save visiting research fellows' list to {file_url}: {e}")

 #---------------------------------------------------------------------------


print("\n>> Fetching and saving visiting research fellows' list...")

# Fetch and save visiting research fellows' list
fellows_raw = get_fellows_list(api_metadata["VISITING_RESEARCH_FELLOWS"]["source"])
fellows = []

if len(fellows_raw) == 0:
    print("No visiting research fellows' data found. Exiting.")
    exit(1)

# Clean up existing visiting research fellows' folders
delete_folder("../images/staff/fellows")

for f in fellows_raw:
    metadata = f.get("metadata", {})

    designations_raw = metadata.get("designations", "")
    designations = [d.strip() for d in designations_raw.split("|") if d.strip()]
    
    remarks_raw = metadata.get("remarks", "")
    remarks = [r.strip() for r in remarks_raw.split("|") if r.strip()]

    fellows.append(
        {
            "name": f.get("name", "").strip(),
            "email": metadata.get("email", "").strip(),
            "position": metadata.get("position", "Visiting Research Fellow").strip(),
            "designations": designations,
            "image": download_image(
                metadata.get("image", "#").strip(),
                "images/staff/fellows",
            ),
            "linkedin": metadata.get("linkedin", "#").strip(),
            "profile": metadata.get("profile", "#").strip(),
            "google_scholar": metadata.get("google_scholar", "#").strip(),
            "researchgate": metadata.get("researchgate", "#").strip(),
            "remarks": remarks
        }
    )


file_url = f"{DIRECTORY}/visiting-research-fellows.json"
save_fellows_list(fellows, file_url, api_metadata["VISITING_RESEARCH_FELLOWS"])
