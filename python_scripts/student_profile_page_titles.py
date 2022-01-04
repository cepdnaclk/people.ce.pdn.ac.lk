# Generate titles for student profile pages based on their name.
# Run this if you want to update the titles of the student profile pages.
# change priority_order if you want to change the order which is taken for the title

# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk

import os


def run():
    foldersPath = "../pages/students/"

    allFolders = os.listdir(foldersPath)
    for eachFolder in allFolders:
        # goes into each folder , E18 E17 etc
        if (eachFolder == "indexPages"):
            continue
        currentStudentFolderPath = foldersPath+eachFolder
        allStudents = os.listdir(currentStudentFolderPath)
        for eachStudent in allStudents:
            # goes into each page, E18098.html etc
            currentStudentPagePath = currentStudentFolderPath + "/" + eachStudent
            contentArray = []
            profPage = open(currentStudentPagePath, "r")
            # read whole content of the page
            contentArray = profPage.read().split("\n")
            profPage.close()
            # save the names in a dictionary
            names = {}
            for eachLine in contentArray:
                if "preferred_long_name" in eachLine and eachLine.split()[-1] != "#":
                    names["preferred_long_name"] = eachLine.split(":")[
                        1].strip()
                if "preferred_short_name" in eachLine and eachLine.split()[-1] != "#":
                    names["preferred_short_name"] = eachLine.split(":")[
                        1].strip()
                if "full_name" in eachLine and eachLine.split()[-1] != "#":
                    names["full_name"] = eachLine.split(":")[1].strip()
                if "name_with_initials" in eachLine and eachLine.split()[-1] != "#":
                    names["name_with_initials"] = eachLine.split(":")[
                        1].strip()
            # priority order the name should be taken in
            priority_order = ['name_with_initials',
                              'preferred_long_name', 'preferred_short_name', 'full_name']
            #  the name that wil be selected
            selected_name = ""
            # select name according to order
            for each in priority_order:
                try:
                    selected_name = names[each]
                    break
                except:
                    continue
            # remove title if existing
            titleRemovedContentArray = []
            for eachLine in contentArray:
                if "title:" in eachLine:
                    continue
                else:
                    titleRemovedContentArray.append(eachLine)
            newTitleAddedContentArray = []
            # add the new title
            for eachLine in titleRemovedContentArray:
                newTitleAddedContentArray.append(eachLine)
                if "permalink" in eachLine:
                    newTitleAddedContentArray.append(f"title: {selected_name}")
            # create new string to write
            contentToWrite = "\n".join(newTitleAddedContentArray)
            writeFile = open(currentStudentPagePath, "w")
            # write to file
            writeFile.write(contentToWrite)
            writeFile.close()


if __name__ == "__main__":
    print("Running")
    run()
