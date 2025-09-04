import os
import shutil

import requests
from PIL import Image  # pip install pillow


def delete_folder(dir_path):
    """Delete the existing folder"""
    try:
        shutil.rmtree(dir_path)
    except FileNotFoundError:
        print(f"Error: Courses Folder Not Found at path: {dir_path}")


def download_image(image_url, save_dir):
    """Download an image from a URL and save it to a local path."""
    try:
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

            try:
                crop_to_square(file_url)
            except Exception as e:
                print(f"Failed to resize image {image_url}: {e}")

    except IOError as e:
        print(f"Failed to save image {image_url} to {save_dir}: {e}")

    return "#"


def crop_to_square(imagePath):
    if imagePath.lower().endswith(".jpg") or imagePath.lower().endswith(".jpeg"):
        image = Image.open(imagePath)
        width, height = image.size
        size = os.path.getsize(imagePath) / 1024
        if size > 25 or (width != height):
            # Resize
            new_width = int(width * 300 / width)
            new_height = int(height * 300 / width)
            resized_image = image.resize((new_width, new_height))

            # Crop - Center
            size = min(new_width, new_height)
            left = (new_width - size) // 2
            upper = (new_height - size) // 2
            right = left + size
            lower = upper + size

            cropped_image = resized_image.crop((left, upper, right, lower))

            if image.size != cropped_image.size:
                cropped_image.save(imagePath)
                print("\t Resized \t {}".format(imagePath))
            else:
                print("\t No resize \t {}".format(imagePath))
    else:
        print("\t Not supported \t {}".format(imagePath))
