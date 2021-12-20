# Generate all image links for docs because theres no time to go into properties of each image and get the dimensions.

# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk

import os
from PIL import Image

filesPath = "../images/docs/"


allFiles = os.listdir(filesPath)
for each in allFiles:
    filePath = filesPath + each
    image = Image.open(filePath)
    width, height = image.size
    print("""{% include documentation_image.html url_image='""" +
          filePath[2:]+"""' text='hi' width='"""+str(width)+"""' height='""" + str(height)+"""' %}""")


"""
Output,

{% include documentation_image.html url_image='/images/docs/change_image_url.PNG' text='hi' width='814' height='876' %}
{% include documentation_image.html url_image='/images/docs/click_edit_inside_github.png' text='hi' width='1904' height='802' %}
{% include documentation_image.html url_image='/images/docs/click_fork.png' text='hi' width='749' height='766' %}
{% include documentation_image.html url_image='/images/docs/click_images.PNG' text='hi' width='678' height='900' %}
{% include documentation_image.html url_image='/images/docs/click_on_commit_msg.PNG' text='hi' width='1038' height='646' %}
{% include documentation_image.html url_image='/images/docs/click_students.PNG' text='hi' width='814' height='795' %}
{% include documentation_image.html url_image='/images/docs/click_your_batch.PNG' text='hi' width='715' height='761' %}
{% include documentation_image.html url_image='/images/docs/commit_changes.PNG' text='hi' width='911' height='591' %}
{% include documentation_image.html url_image='/images/docs/copy_new_file_path.PNG' text='hi' width='844' height='817' %}
{% include documentation_image.html url_image='/images/docs/copy_paste_text.PNG' text='hi' width='1825' height='864' %}
{% include documentation_image.html url_image='/images/docs/create_new_file.PNG' text='hi' width='1875' height='677' %}
{% include documentation_image.html url_image='/images/docs/create_pull_req.png' text='hi' width='1848' height='686' %}
{% include documentation_image.html url_image='/images/docs/create_pull_req2.png' text='hi' width='1399' height='701' %}
{% include documentation_image.html url_image='/images/docs/drag_and_drop.PNG' text='hi' width='1777' height='833' %}
{% include documentation_image.html url_image='/images/docs/edit_file.PNG' text='hi' width='1817' height='768' %}
{% include documentation_image.html url_image='/images/docs/edit_this_on_github.png' text='hi' width='1348' height='772' %}
{% include documentation_image.html url_image='/images/docs/file_name.PNG' text='hi' width='1112' height='566' %}
{% include documentation_image.html url_image='/images/docs/get_clone_url.png' text='hi' width='1866' height='657' %}
{% include documentation_image.html url_image='/images/docs/name_with_intials.png' text='hi' width='1677' height='762' %}
{% include documentation_image.html url_image='/images/docs/open_pull_request.PNG' text='hi' width='1284' height='781' %}
{% include documentation_image.html url_image='/images/docs/pages.PNG' text='hi' width='856' height='855' %}
{% include documentation_image.html url_image='/images/docs/propose_changes.png' text='hi' width='715' height='403' %}
{% include documentation_image.html url_image='/images/docs/propose_new_file.PNG' text='hi' width='865' height='661' %}
{% include documentation_image.html url_image='/images/docs/pull_req_title.PNG' text='hi' width='1412' height='880' %}
{% include documentation_image.html url_image='/images/docs/search_reg_no.PNG' text='hi' width='1706' height='553' %}
{% include documentation_image.html url_image='/images/docs/shift_right_click_open_linux.png' text='hi' width='503' height='670' %}
{% include documentation_image.html url_image='/images/docs/studentDetails_description.png' text='hi' width='1643' height='870' %}
{% include documentation_image.html url_image='/images/docs/students.PNG' text='hi' width='825' height='790' %}
{% include documentation_image.html url_image='/images/docs/upload_files.PNG' text='hi' width='1260' height='723' %}
"""
