# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk
import json
for x in range(2, 14):
    jsonLink = f"../../_data/stud/e{x:02}.json"
    jsonData = dict(json.load(open(jsonLink)))

    newJSON = {}
    for each in jsonData:
        newdata = jsonData[each]
        # edited this to remove the curent aff line
        try:
            newdata.pop("current_affliation")
        except:
            print("current aff not in file")
        newJSON[each] = newdata

    writeFile = open(jsonLink, "w")
    writeFile.write(json.dumps(newJSON, indent=4))
