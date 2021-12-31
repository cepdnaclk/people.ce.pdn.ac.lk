# Remove Mr, Miss from E18, E17, E16 profile pages #67
# https://github.com/cepdnaclk/people.ce.pdn.ac.lk/issues/67

# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk

import os

filesPath = "../pages/students/e16/"


allFiles = os.listdir(filesPath)
for each in allFiles:
    filePath = filesPath + each
    thisFile = open(filePath, "r")
    fileContents = thisFile.read()
    thisFile.close()
    splitted = fileContents.split("\n")

    newArray = []
    for eachLine in splitted:
        splitted = eachLine.split()
        if "Mr" in splitted :
            splitted.remove("Mr")
        if "Miss" in splitted:
            splitted.remove("Miss")
        newArray.append(" ".join(splitted))
        

    newContent = "\n".join(newArray)

    thisFile = open(filePath, "w")
    thisFile.write(newContent)
    thisFile.close()