# Generate html pages from csv
# Author: E/17/154 Akilax0 - e17154@eng.pdn.ac.lk

import csv


BATCH = '22'
CSV = 'Book1.csv'

with open(CSV, mode ='r') as file:    
       csvFile = csv.reader(file)
       next(csvFile)
       next(csvFile)
       for lines in csvFile:
            eno = lines[1]
            name = lines[2]
            email = lines[4]
           
            eno_strip = eno.replace('/','') 
            # regNo = int(eno[-3:]) 
            print(eno,eno_strip,name,email)

            htmlFile = open(f"../../../pages/students/e{BATCH}/e{eno_strip[1:]}.html", 'w+')
            text = f"""---
layout: studentDetails
permalink: "/students/e{BATCH}/{eno_strip[3:]}/"
title: {name}


reg_no: E/{BATCH}/{eno_strip[-3:]}
batch: E{BATCH}

department: Computer Engineering
current_affiliation: Department of Computer Engineering, University of Peradeniya

full_name: {name}
name_with_initials: {name}
preferred_short_name: {name}
preferred_long_name: #
honorific: #

email_faculty: {email}
email_personal: #

location: #

url_cv: #
url_website: #
url_linkedin: #
url_github: #
url_facebook: #
url_researchgate: #
url_twitter: #

interests: #

image_url: "images/students/e{BATCH}/e{eno_strip[1:]}.JPG"

---
            """
            htmlFile.write(text)
            htmlFile.close()
