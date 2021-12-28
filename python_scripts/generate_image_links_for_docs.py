# Generate all image links for docs because theres no time to go into properties of each image and get the dimensions.

# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk

import os
from PIL import Image
import json

filesPath = "../images/docs/"

data_images = "../_data/images.json"
data_imagesFile = open(data_images, "w")
dataDict = {}


allFiles = os.listdir(filesPath)
for each in allFiles:
    filePath = filesPath + each
    image = Image.open(filePath)
    width, height = image.size
    print("""{% include documentation_image.html url_image='""" +
          filePath[2:]+"""' text='hi' %}""")
    dataDict[each] = {"width": width, "height": height}

data_imagesFile.write(json.dumps(dataDict, indent=4))

"""
Output,

{% include documentation_image.html url_image='/images/docs/change_image_url.PNG' text='hi' %}
{% include documentation_image.html url_image='/images/docs/click_edit_inside_github.png' text='hi' %}
{% include documentation_image.html url_image='/images/docs/click_fork.png' text='hi' %}
{% include documentation_image.html url_image='/images/docs/click_images.PNG' text='hi' %}
{% include documentation_image.html url_image='/images/docs/click_on_commit_msg.PNG' text='hi' %}
{% include documentation_image.html url_image='/images/docs/click_students.PNG' text='hi' %}
{% include documentation_image.html url_image='/images/docs/click_your_batch.PNG' text='hi' %}
{% include documentation_image.html url_image='/images/docs/commit_changes.PNG' text='hi' %}
{% include documentation_image.html url_image='/images/docs/copy_new_file_path.PNG' text='hi' %}
{% include documentation_image.html url_image='/images/docs/copy_paste_text.PNG' text='hi' %}
{% include documentation_image.html url_image='/images/docs/create_new_file.PNG' text='hi' %}
{% include documentation_image.html url_image='/images/docs/create_pull_req.png' text='hi' %}
{% include documentation_image.html url_image='/images/docs/create_pull_req2.png' text='hi' %}
{% include documentation_image.html url_image='/images/docs/drag_and_drop.PNG' text='hi' %}
{% include documentation_image.html url_image='/images/docs/edit_file.PNG' text='hi' %}
{% include documentation_image.html url_image='/images/docs/edit_this_on_github.png' text='hi' %}
{% include documentation_image.html url_image='/images/docs/file_name.PNG' text='hi' %}
{% include documentation_image.html url_image='/images/docs/get_clone_url.png' text='hi' %}
{% include documentation_image.html url_image='/images/docs/name_with_intials.png' text='hi' %}
{% include documentation_image.html url_image='/images/docs/open_pull_request.PNG' text='hi' %}
{% include documentation_image.html url_image='/images/docs/pages.PNG' text='hi' %}
{% include documentation_image.html url_image='/images/docs/propose_changes.png' text='hi' %}
{% include documentation_image.html url_image='/images/docs/propose_new_file.PNG' text='hi' %}
{% include documentation_image.html url_image='/images/docs/pull_req_title.PNG' text='hi' %}
{% include documentation_image.html url_image='/images/docs/search_reg_no.PNG' text='hi' %}
{% include documentation_image.html url_image='/images/docs/shift_right_click_open_linux.png' text='hi' %}
{% include documentation_image.html url_image='/images/docs/studentDetails_description.png' text='hi' %}
{% include documentation_image.html url_image='/images/docs/students.PNG' text='hi' %}
{% include documentation_image.html url_image='/images/docs/upload_files.PNG' text='hi' %}
"""
