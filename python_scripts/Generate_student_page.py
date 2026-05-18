import csv
import os
from tkinter import Tk, filedialog

def pick_csv_file():
    root = Tk()
    root.withdraw()
    return filedialog.askopenfilename(
        title="Select E24 CSV file",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )

def run():
    csv_path = pick_csv_file()
    if not csv_path:
        print("No CSV selected.")
        return

    output_dir = os.path.join("..", "pages", "students", "e24")
    os.makedirs(output_dir, exist_ok=True)

    with open(csv_path, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            reg_no_raw = row["E/Number"].strip()     # E/24/007
            name = row["Name with Initials"].strip()
            email = row["Email Address"].strip()

            parts = reg_no_raw.split("/")
            if len(parts) != 3:
                print(f"Skipping invalid reg no: {reg_no_raw}")
                continue

            batch = parts[1].lower()   # 24
            reg_no = parts[2]          # 007

            page_path = os.path.join(output_dir, f"e{batch}{reg_no}.html")

            content = f"""---
layout: studentDetails
permalink: "/students/e{batch}/{reg_no}/"
title: {name}

reg_no: E/{batch.upper()}/{reg_no}
batch: E{batch.upper()}

department: "Computer Engineering"
current_affiliation: "Department of Computer Engineering"

full_name: {name}
name_with_initials: {name}
preferred_short_name: {name}
preferred_long_name: {name}
honorific: #

email_faculty: {email}
email_personal: #

location: "#"

url_cv: #
url_website: #
url_linkedin: #
url_github: #
url_facebook: #
url_researchgate: #
url_twitter: #


interests: "#"

image_url: images/students/e{batch}/e{batch}{reg_no}.jpg
---

"""

            with open(page_path, "w", encoding="utf-8") as out:
                out.write(content)

            print(f"Created {page_path}")

if __name__ == "__main__":
    run()