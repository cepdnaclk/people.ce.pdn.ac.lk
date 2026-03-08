# Sync Jekyll site content to Algolia for search indexing.

# Author: E/15/150 Nuwan Jaliyagoda - nuwanjaliyagoda@eng.pdn.ac.lk

import json
import os
import sys
from pathlib import Path

import yaml
from algoliasearch.search_client import SearchClient
from util.configs import STAFF_IDX_SETTINGS, STUDENTS_IDX_SETTINGS
from util.helpers import load_env_var, safe_str

BUILD_DIR = Path(os.environ.get("JEKYLL_BUILD_DIR", "_site"))


def load_student_profiles():
    """
    Load student profiles from Jekyll pages, parse their frontmatter and content, and return a list of records.
    """
    students_dir = Path("../pages") / "students"
    output_path = Path("../_data") / "temp" / "students.json"

    records = []
    for file_path in students_dir.rglob("*.html"):
        text = file_path.read_text(encoding="utf-8")
        front_matter = ""
        content = text
        if text.startswith("---"):
            parts = text.split("---", 2)
            if len(parts) >= 3:
                front_matter = parts[1]
                content = parts[2].lstrip("\n")
            else:
                front_matter = None
                content = ""

        if front_matter is None:
            # Skip processing if no frontmatter there
            continue

        metadata = yaml.safe_load(front_matter) or {}
        if not isinstance(metadata, dict):
            metadata = {"front_matter": metadata}

        if "permalink" not in metadata:
            # Skip if permalink is missing, as it's essential for URL generation
            continue

        record = {
            "objectID": f"student_{str(metadata.get('reg_no', '')).strip().replace('/', '')}",
            "url": safe_str(metadata["permalink"]),
            "role": "Student",
            "title": safe_str(metadata.get("title", "")),
            "interests": [
                str(cat).strip()
                for cat in str(metadata.get("interests")).split(",")
                if metadata.get("interests")
            ]
            or [],
            "batch": safe_str(metadata.get("batch", "")),
            "reg_no": safe_str(metadata.get("reg_no", "")),
            "current_affiliation": safe_str(metadata.get("current_affiliation", "")),
            "name_formats": {
                "full_name": safe_str(metadata.get("full_name", "")),
                "name_with_initials": safe_str(metadata.get("name_with_initials", "")),
                "preferred_short_name": safe_str(
                    metadata.get("preferred_short_name", "")
                ),
                "preferred_long_name": safe_str(
                    metadata.get("preferred_long_name", "")
                ),
                "honorific": safe_str(metadata.get("honorific", "")),
            },
            "department": safe_str(metadata.get("department", "")),
            "location": safe_str(metadata.get("location", "")),
            "metadata": {
                "urls": {
                    "website": safe_str(metadata.get("url_website")),
                    "linkedin": safe_str(metadata.get("url_linkedin")),
                    "github": safe_str(metadata.get("url_github")),
                    "facebook": safe_str(metadata.get("url_facebook")),
                    "researchgate": safe_str(metadata.get("url_researchgate")),
                    "twitter": safe_str(metadata.get("url_twitter")),
                },
                "emails": {
                    "personal": safe_str(metadata.get("email_personal", "")),
                    "university": safe_str(metadata.get("email_faculty", "")),
                },
            },
            "content": safe_str(content),
        }
        records.append(record)

    # Note: This is a temporary step, only for development and testing.
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    return records


def load_staff_profiles():
    """
    Load staff profiles from Jekyll pages and temporary JSON, and combine them into a single list of records.
    """
    staff_dir = Path("../pages") / "staff" / "academic-staff"
    temp_staff_path = Path("../_data") / "temporary_academic_staff.json"
    output_path = Path("../_data") / "temp" / "staff.json"

    records = []

    for file_path in staff_dir.rglob("*.html"):
        text = file_path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue

        parts = text.split("---", 2)
        if len(parts) < 3:
            continue

        metadata = yaml.safe_load(parts[1]) or {}
        if not isinstance(metadata, dict):
            continue

        if "permalink" not in metadata:
            # Skip if permalink is missing, as it's essential for URL generation
            continue

        research_interests = metadata.get("research_interests") or []
        if not isinstance(research_interests, list):
            research_interests = [research_interests]

        records.append(
            {
                "objectID": f"staff_{file_path.stem}",
                "url": safe_str(metadata.get("permalink", "")),
                "role": "Academic Staff",
                "title": safe_str(metadata.get("title", "")),
                "interests": [safe_str(item) for item in research_interests if item]
                or [],
                "batch": None,
                "reg_no": None,
                "current_affiliation": safe_str(metadata.get("designation", "")),
                "name_formats": {
                    "full_name": safe_str(metadata.get("title", "")),
                    "name_with_initials": None,
                    "preferred_short_name": None,
                    "preferred_long_name": None,
                    "honorific": None,
                },
                "department": "Computer Engineering",
                "location": None,
                "metadata": {
                    "urls": {
                        "website": safe_str(metadata.get("url_website")),
                        "linkedin": safe_str(metadata.get("url_linkedin")),
                        "researchgate": safe_str(metadata.get("url_researchgate")),
                        "google_scholar": safe_str(metadata.get("url_google_scholar")),
                        "orcid": safe_str(metadata.get("url_orcid")),
                        "ad_scientific_index": safe_str(
                            metadata.get("url_ad_scientific_index")
                        ),
                    },
                    "emails": {
                        "university": safe_str(metadata.get("email", "")),
                    },
                },
                "content": safe_str(parts[2].lstrip("\n")),
            }
        )

    temp_staff = json.loads(temp_staff_path.read_text(encoding="utf-8")).get("data", [])
    for staff in temp_staff:
        email = safe_str(staff.get("email", ""))
        staff_name = safe_str(staff.get("staff_name", ""))
        records.append(
            {
                "objectID": f"temp_staff_{email or safe_str(staff.get('staff_name', '')).lower().replace(' ', '_')}",
                "url": f"/staff/temporary-academic-staff/#:~:text={staff_name.replace(' ', '%20')}",
                "role": "Temporary Academic Staff",
                "title": staff_name,
                "interests": [],
                "batch": None,
                "reg_no": None,
                "name_formats": {"full_name": safe_str(staff.get("staff_name", ""))},
                "department": "Computer Engineering",
                "location": None,
                "metadata": {
                    "urls": {
                        "linkedin": safe_str(staff.get("linkedin")),
                    },
                    "emails": {
                        "university": email,
                    },
                },
            }
        )

    existing_records = []
    if output_path.exists():
        existing_records = json.loads(output_path.read_text(encoding="utf-8"))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps([*existing_records, *records], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    return records


def sync(index, records, settings):
    MAX_CONTENT = 1000

    # Truncate large content fields
    updated_records = []

    for rec in records:
        # No longer chunking content - just truncate to max length

        # content = rec.get("content")
        # if isinstance(content, str) and len(content) > MAX_CONTENT:
        #     # Split oversized content into multiple chunked records
        #     start = 0
        #     chunk_idx = 1
        #     while start < len(content):
        #         chunk_content = content[start : start + MAX_CONTENT]
        #         new_rec = rec.copy()
        #         new_rec["content"] = chunk_content
        #         new_rec["chunk"] = chunk_idx
        #         if "objectID" in rec:
        #             new_rec["objectID"] = f"{rec['objectID']}#c{chunk_idx}"
        #         updated_records.append(new_rec)
        #         start += MAX_CONTENT
        #         chunk_idx += 1
        #     continue

        if rec.get("content"):
            rec["content"] = rec.get("content").strip()[:MAX_CONTENT]

        updated_records.append(rec)

    print(
        f"Uploading {len(records)} records to '{index.name}' via {len(updated_records)} chunks"
    )

    r = index.replace_all_objects(updated_records)
    if isinstance(r, dict) and "taskID" in r:
        index.wait_task(r["taskID"])
    r = index.set_settings(settings)
    if isinstance(r, dict) and "taskID" in r:
        index.wait_task(r["taskID"])
    print(f"Completed '{index.name}'")


def main():
    try:
        client = SearchClient.create(
            app_id=load_env_var("ALGOLIA_APP_ID"),
            api_key=load_env_var("ALGOLIA_ADMIN_API_KEY"),
        )

        # Student Profiles
        student_profiles = load_student_profiles()
        sync(
            client.init_index("student_profiles"),
            student_profiles,
            STUDENTS_IDX_SETTINGS,
        )

        # Staff Profiles
        staff_profiles = load_staff_profiles()
        sync(
            client.init_index("staff_profiles"),
            staff_profiles,
            STAFF_IDX_SETTINGS,
        )
        return 0

    except Exception as e:
        print(f"Algolia sync failed: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
