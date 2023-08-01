# Resize all student images to make their size smaller
# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk

import os
from PIL import Image  # pip install pillow


def crop_to_square(imagePath):
    image = Image.open(imagePath)
    width, height = image.size
    size = os.path.getsize(imagePath) / 1024
    if size > 25 or (width != height):
        # Resize
        new_width = int(width * 300 / width)
        new_height = int(height * 300 / width)
        resized_image = image.resize((new_width, new_height))

        # Crop
        size = min(new_width, new_height)
        left = (width - size) // 2
        upper = (height - size) // 2
        right = left + size
        lower = upper + size

        cropped_image = resized_image.crop((left, upper, right, lower))

        if image.size != cropped_image.size:
            cropped_image.save(imagePath)
            print("\t {} Resized and cropped".format(imagePath))
        else:
            print("\t {} No resize required".format(imagePath))


def run():
    imagesPath = "../images/students"
    directory_list = os.listdir(imagesPath)

    for eachFolder in directory_list:
        if "." in eachFolder:
            continue  # skip if not folder

        for eachImage in os.listdir(imagesPath + f"/{eachFolder}"):
            if eachImage == "e16172.jpg" or eachImage == "e18366.jpg":
                continue  # this was a png so the resizing doesnt work properly

            try:
                imagePath = imagesPath + f"/{eachFolder}/{eachImage}"
                crop_to_square(imagePath)

            except Exception as e:
                print(f"\t Failed to resize image {imagePath}, {e}")


if __name__ == "__main__":
    run()
