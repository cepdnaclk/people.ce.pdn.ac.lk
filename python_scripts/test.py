# This is used to test small bits of code

import gdown
from PIL import Image  # pip install pillow
import os 

image_url = "https://drive.google.com/open?id=1YWnYz6wAMIa54NgzAGDcYlDzrUQ8F7xc"
returnValue = gdown.download("https://drive.google.com/uc?id=" +
                           image_url.split("=")[1].strip(), "./", quiet=True)
image = Image.open(returnValue)
image.save("test.jpg")
os.system("rm '"+returnValue + "'")