# Adds "/" at the end of permalink to solve issue46
# https://github.com/cepdnaclk/people.ce.pdn.ac.lk/issues/46

## Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk


import os

filesPath = "../pages/students/e14/"


allFiles = os.listdir(filesPath)
for each in allFiles:
    filePath = filesPath + each
    thisFile = open(filePath, "r")
    fileContents = thisFile.read()
    thisFile.close()
    splitted = fileContents.split("\n")

    newArray = []
    for eachLine in splitted:
        if "permalink" not in eachLine:
            newArray.append(eachLine)
            continue

        if eachLine[-2] == "/":
            print("/ is already there")
            exit()
        eachLine = eachLine[0:-1] + "/" + eachLine[-1]
        newArray.append(eachLine)

    newContent = "\n".join(newArray)

    thisFile = open(filePath, "w")
    thisFile.write(newContent)


