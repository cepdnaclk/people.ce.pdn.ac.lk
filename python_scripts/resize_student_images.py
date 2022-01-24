# Resize all student images to make their size smaller
# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk

import os
from PIL import Image # pip install pillow

def run():
    imagesPath = "../images/students"
    directory_list = os.listdir(imagesPath)

    for eachFolder in directory_list:
        if "." in eachFolder:
            continue  # skip if not folder
        for eachImage in os.listdir(imagesPath+f"/{eachFolder}"):
            try:
                imagePath = imagesPath+f"/{eachFolder}/{eachImage}"
                image = Image.open(imagePath)
                width, height = image.size
                size = os.path.getsize(imagePath)/1024
                if size > 25:
                    print(f"{imagePath}, width = {width:5}, height = {height:5}, size = {size:4.4}kb")
                    resizeValue = 300/width
                    new_image = image.resize((int(width*resizeValue), int(height*resizeValue)))

                    if(not (int(width*resizeValue) == width and int(height*resizeValue) == height)):
                        new_image.save(imagePath)
                    else:
                        print("No resize required")
            except:
                print(f"Failed to resize image {imagePath}")

if __name__ == "__main__":
    run()
