import collections
import json

jsonPath = "../_data/stud/e2a.json"

jsonDict = json.load(open(jsonPath))
orderedDict = collections.OrderedDict(sorted(jsonDict.items()))

with open(jsonPath, "w") as outfile:
    json.dump(orderedDict, outfile, indent=2)
