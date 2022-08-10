1) login to feels and copy the cookie "MoodleSessionfeels" into python_scripts/add_new_student_batch/1_feelsGetUser.py line 17 (cookieyes.com/blog/how-to-check-cookies-on-your-website-manually/)
2) Run the script ("python3 1_feelsGetUser.py") this will take some time. This will output all details to batch_all.txt file
3) Create the new folder at pages/students for the html files
    for example if the new batch is e19. create  the folder pages/students/e19
4) Create a new folder for the images at images/students/
    if the new batch is e19, create the folder images/students/e19
5) In script 2_download_image_gen_html
    Replace all Exx with the correct batch name
        line 22 urllib.request.urlretrieve(link, f"../../images/students/exx/e{regNo}.jpg") -> urllib.request.urlretrieve(link, f"../../images/students/e19/e{regNo}.jpg")
        line 24 htmlFile = open(f"../../pages/students/e19/e{int(regNo):03d}.html", "w")
        line 27 permalink: "/students/e19/{int(regNo[2:]):03d}/"
        line 29 and 30
        line 38
        line 42
6) run script 2 ("python3 python3 2_download_image_gen_html.py")