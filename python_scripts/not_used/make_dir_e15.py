"""
Author : Akilax0

The script reads through csv files @
    /csv
and creates batch folders @
    /pages/students
if not already available.
"""

#import modules
import csv
import os

# assign directory
src_path = '../_csv'
dest_path = '../pages/students/'


def writeHTML(permalink, enum, batch, full_name, name_initial, pref_short_name, pref_long_name, honor, fac_email, per_email, location, url_cv, url_website, url_linked, url_github, url_fb, url_research, twitter, image_url):

    # Note change parameters to required changes in the template

    s = """---
layout: studentDetails
permalink: \"""" + permalink + """\"

reg_no: """ + enum + """
batch: """ + batch + """

full_name: """ + full_name + """
name_with_initials: """ + name_initial + """
preferred_short_name: """ + pref_short_name + """
preferred_long_name: """ + pref_long_name + """
honorific: """ + honor + """

email_faculty: """ + fac_email + """
email_personal: """ + per_email + """

location: """ + location + """

url_cv: """ + url_cv + """
url_website: """ + url_website + """
url_linkedin: """ + url_linked + """
url_github: """ + url_github + """
url_facebook: """ + url_fb + """
url_researchgate: """ + url_research + """
url_twitter: """ + twitter + """

projects_done: []
image_url: """ + image_url + """
---
"""
    return s


if(os.path.isdir(src_path) == False):
    print("Unavailable source directory")
    exit(0)


# iterate over files in directory
for filename in os.scandir(src_path):
    if filename.is_file():
        with open(filename.path, mode='r')as file:
          # reading the CSV file
            csvFile = csv.reader(file)

            for lines in csvFile:
                temp = lines[0].split('/')

                # checks for redundant lines
                if(len(temp) != 3):
                    continue

                batch = 'e' + temp[1]
                enum = batch + temp[2]
                file_name = enum + '.html'

                permalink = "/students/" + batch + "/" + temp[2]

                long_name = lines[2]
                short_name = long_name.split(' ')[0]
                image_url = "images/students/"+batch+"/" + enum + ".jpg"

                email_faculty = enum + '@ce.pdn.ac.lk'
                print(enum, file_name, dest_path+batch)

                if(os.path.isdir(dest_path+batch) == False):
                    os.mkdir(dest_path+batch)

                with open(os.path.join(dest_path+batch, file_name), 'w') as fp:
                    # permalink,enum,batch,full_name,name_initial,pref_short_name,pref_long_name,honor,fac_email,per_email,location,url_cv,url_website,url_linked,url_github,url_fb,url_research,twitter
                    fp.write(writeHTML(permalink, lines[0], temp[0]+temp[1], lines[2], "#", short_name, long_name, "#",
                             email_faculty, "#", "#", "#", "#", "#", "https://github.com/"+lines[4], "#", "#", "#", image_url))
