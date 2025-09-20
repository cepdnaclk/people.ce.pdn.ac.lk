# Create json file in _data/stud/*.json + download image using information taken from javascript code
#  https://cepdnaclk.github.io/department-website-2013/people/e08.html
# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk

# run js on site
"""
output = {};
list1 = document.getElementsByTagName("tr");
let count = 0;
for (let i = 0; i < list1.length; i=i+2) {
  console.log(count)
  output[count] = { name : list1[i].getElementsByTagName("th")[0].innerText , image : list1[i].getElementsByTagName("th")[1].getElementsByTagName("img")[0].src }
  count = count + 1;
  output[count] = { name : list1[i].getElementsByTagName("th")[3].innerText , image : list1[i].getElementsByTagName("th")[4].getElementsByTagName("img")[0].src }
  count = count + 1;
}
JSON.stringify(output)
"""

import json
import urllib.request

# the output,

outputFromJavaScript = """
{"0":{"name":"E/03/002 - D.M.A. Abeyratne","image":"https://none.comsd"},"1":{"name":"E/03/027 - L.N.K. Atapattu","image":"https://none.comsd"},"2":{"name":"E/03/031 - B.A.N.M. Bambarasinghe","image":"https://none.comsd"},"3":{"name":"E/03/035 - M.D.M.E.L.S. Bandara","image":"https://none.comsd"},"4":{"name":"E/03/037 - R.M.W.S. Bandara","image":"https://none.comsd"},"5":{"name":"E/03/042 - U.P. Bulumulla","image":"https://none.comsd"},"6":{"name":"E/03/050 - U.D.H.U. Dewapriya","image":"https://none.comsd"},"7":{"name":"E/03/066 - M.I. Fernando","image":"https://none.comsd"},"8":{"name":"E/03/068 - W.I.B. Fernando","image":"https://none.comsd"},"9":{"name":"E/03/074 - G.A.S.S. Ganepola","image":"https://none.comsd"},"10":{"name":"E/03/082 - J.M.N.C. Gunawardana","image":"https://none.comsd"},"11":{"name":"E/03/092 - H.M.S. Hurugammuwa","image":"https://none.comsd"},"12":{"name":"E/03/101 - R.A.A. Ireshika","image":"https://none.comsd"},"13":{"name":"E/03/103 - G.P. Ishara","image":"https://none.comsd"},"14":{"name":"E/03/121 - K.G.M.S.K. Jayawardana","image":"https://none.comsd"},"15":{"name":"E/03/126 - T.N. Kadurugamuwa","image":"https://none.comsd"},"16":{"name":"E/03/127 - S.U. Kahawatta","image":"https://none.comsd"},"17":{"name":"E/03/128 - B. Kajakaran","image":"https://none.comsd"},"18":{"name":"E/03/134 - K.W.L.K. Karunarathne","image":"https://none.comsd"},"19":{"name":"E/03/135 - W.S.B. Karunathilaka","image":"https://none.comsd"},"20":{"name":"E/03/137 - K. Balasundaram","image":"https://none.comsd"},"21":{"name":"E/03/142 - M.D.D.U. Kulathunga","image":"https://none.comsd"},"22":{"name":"E/03/147 - K.P.N.R.R. Kumara","image":"https://none.comsd"},"23":{"name":"E/03/150 - V.P. Kumara","image":"https://none.comsd"},"24":{"name":"E/03/153 - K.P.S.D. Kumarapathirana","image":"https://none.comsd"},"25":{"name":"E/03/158 - M.S.C. Lakshman","image":"https://none.comsd"},"26":{"name":"E/03/162 - A.A. Madawala","image":"https://none.comsd"},"27":{"name":"E/03/166 - M.R.B.P. Malwana","image":"https://none.comsd"},"28":{"name":"E/03/176 - M.A.G.S. Munasinghe","image":"https://none.comsd"},"29":{"name":"E/03/177 - M.A.M.D.P. Munasinghe","image":"https://none.comsd"},"30":{"name":"E/03/184 - Ganeshan Narmatha","image":"https://none.comsd"},"31":{"name":"E/03/185 - H.M.R.D.B. Navarathna","image":"https://none.comsd"},"32":{"name":"E/03/187 - J. Neera","image":"https://none.comsd"},"33":{"name":"E/03/218 - R.A.A. Rajapaksha","image":"https://none.comsd"},"34":{"name":"E/03/243 - M.A.A. Sandaruwan","image":"https://none.comsd"},"35":{"name":"E/03/257 - V. Sivalingam","image":"https://none.comsd"},"36":{"name":"E/03/270 - V. Vijayarathna","image":"https://none.comsd"},"37":{"name":"E/03/276 - N.M. Warnasuriya","image":"https://none.comsd"},"38":{"name":"E/03/281 - M.G. Weerarathna","image":"https://none.comsd"},"39":{"name":"E/02/117 - A.M.B.R.B. Jayathilake","image":"https://none.comsd"}}

"""

data = json.loads(outputFromJavaScript)
outputJSON = {}

for i in range(len(data)):
    name = data[str(i)]["name"]
    batch = int(name[2:4])
    regNo = int(name[5 : 5 + 3])
    url = data[str(i)]["image"]
    name = name.split("-")[1].strip()
    print(name, batch, regNo, url)
    image_path = f"images/students/e{str(batch).zfill(2)}/e{str(batch).zfill(2)}{str(regNo).zfill(3)}.jpg"
    try:
        urllib.request.urlretrieve(url, "../" + image_path)
    except:
        image_path = "images/students/default.jpg"
    outputJSON[str(f"E/{str(batch).zfill(2)}/{str(regNo).zfill(3)}")] = {
        "reg_no": f"E/{str(batch).zfill(2)}/{str(regNo).zfill(3)}",
        "name_with_initials": name,
        "image_url": image_path,
    }


outputJSONFile = open(f"../_data/stud/e{str(batch).zfill(2)}.json", "w")
outputJSONFile.write(json.dumps(outputJSON, indent=2))
outputJSONFile.close()
