# Inserts interests into profile pages to solve issue47
# https://github.com/cepdnaclk/people.ce.pdn.ac.lk/issues/47


import os

filesPath = "../pages/students/e17/"


allFiles = os.listdir(filesPath)
for each in allFiles:
    filePath = filesPath + each
    thisFile = open(filePath, "r")
    fileContents = thisFile.read()
    thisFile.close()
    splitted = fileContents.split("\n")

    newArray = []
    for eachLine in splitted:
        if "projects_done" not in eachLine:
            newArray.append(eachLine)
            continue

        newArray.append("interests: #")
        newArray.append(eachLine)

    newContent = "\n".join(newArray)

    thisFile = open(filePath, "w")
    thisFile.write(newContent)
    thisFile.close()
