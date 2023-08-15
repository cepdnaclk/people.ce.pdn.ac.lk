# Resize all student images to make their size smaller
# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk

import os
from PIL import Image  # pip install pillow
from util.crop import crop_to_square


def run():
    imagesPath = "../images/students"
    directory_list = os.listdir(imagesPath)

    for eachFolder in directory_list:
        if "." in eachFolder:
            continue  # skip if not folder

        for eachImage in os.listdir(imagesPath + f"/{eachFolder}"):
            try:
                imagePath = imagesPath + f"/{eachFolder}/{eachImage}"
                crop_to_square(imagePath)
            except Exception as e:
                print(f"\t Failed to resize image {imagePath}, {e}")


if __name__ == "__main__":
    run()
