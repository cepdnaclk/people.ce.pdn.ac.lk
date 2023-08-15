import os
from PIL import Image  # pip install pillow


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
            upper = (new_height - size) // 4
            right = left + size
            lower = upper + size

            cropped_image = resized_image.crop((left, upper, right, lower))

            if image.size != cropped_image.size:
                cropped_image.save(imagePath)
                print("\t Resized \t {}".format(imagePath))
            else:
                print("\t {} No resize \t {}".format(imagePath))
    else:
        print("\t Not supported \t {}".format(imagePath))
