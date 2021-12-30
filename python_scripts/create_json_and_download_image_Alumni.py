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

import urllib.request
import json


# the output,

outputFromJavaScript = """
{"0":{"name":"e03249 - S.W.B.Sanjeewa","image":"htts://none.com"},"1":{"name":"e04001 - M.L.S.Abeyratha","image":"htts://none.com"},"2":{"name":"e04010 - A.M.E.N.Adikari","image":"htts://none.com"},"3":{"name":"e04015 - A.P.H.I.Alexander","image":"htts://none.com"},"4":{"name":"e04032 - B.M.D.Balasuriya","image":"htts://none.com"},"5":{"name":"e04038 - M.P.Bandara","image":"htts://none.com"},"6":{"name":"e04043 - W.R.A.S.N.Bandara","image":"htts://none.com"},"7":{"name":"e04047 - T.M.S.Buddika","image":"htts://none.com"},"8":{"name":"e04058 - L.I.Dasanayake","image":"htts://none.com"},"9":{"name":"e04059 - D.M.C.Dassanayake","image":"htts://none.com"},"10":{"name":"e04065 - R.D.I.P.Devinda","image":"htts://none.com"},"11":{"name":"e04110 - N.M.Herath","image":"htts://none.com"},"12":{"name":"e04111 - R.N.B.Herath","image":"htts://none.com"},"13":{"name":"e04112 - H.A.B.L.Hettiarachchi","image":"htts://none.com"},"14":{"name":"e04114 - M.N.A.Hinas","image":"htts://none.com"},"15":{"name":"e04116 - P.Ilanthirayan","image":"htts://none.com"},"16":{"name":"e04120 - J.R.S.T.B.Jayalath","image":"htts://none.com"},"17":{"name":"e04123 - W.D.S.Jayarathna","image":"htts://none.com"},"18":{"name":"e04131 - W.M.H.S.Jayasuriya","image":"htts://none.com"},"19":{"name":"e04143 - A.A.M.M.E.Karunarathna","image":"htts://none.com"},"20":{"name":"e04145 - A.K.B.Karunathilake","image":"htts://none.com"},"21":{"name":"e04153 - A.P.D.Krishnajith","image":"htts://none.com"},"22":{"name":"e04171 - D.R.Lunugalage","image":"htts://none.com"},"23":{"name":"e04191 - A.Neleththige","image":"htts://none.com"},"24":{"name":"e04192 - S.D.Nelson","image":"htts://none.com"},"25":{"name":"e04196 - J.Nivethan","image":"htts://none.com"},"26":{"name":"e04204 - A.K.S.Pemarathne","image":"htts://none.com"},"27":{"name":"e04220 - R.D.N.Priyathilaka","image":"htts://none.com"},"28":{"name":"e04221 - K.Puwanasunthara","image":"htts://none.com"},"29":{"name":"e04223 - R.M.S.D.Rajapaksha","image":"htts://none.com"},"30":{"name":"e04238 - R.M.R.S.Rathnayake","image":"htts://none.com"},"31":{"name":"e04253 - A.Sampasivamoorthy","image":"htts://none.com"},"32":{"name":"e04256 - R.Sanjaiyan","image":"htts://none.com"},"33":{"name":"e03025 - M.M.M.Arsath","image":"htts://none.com"},"34":{"name":"e04264 - R.W.M.L.C.P.Senanayake","image":"htts://none.com"},"35":{"name":"e04268 - S.M.P.T.K.Senevirathne","image":"htts://none.com"},"36":{"name":"e04270 - D.W.M.H.W.D.N.Seneviratne","image":"htts://none.com"},"37":{"name":"e04273 - R.Sheerasagar","image":"htts://none.com"},"38":{"name":"e04277 - K.V.N.M.Singaghosha","image":"htts://none.com"},"39":{"name":"e04289 - K.I.P.Sugathsiri","image":"htts://none.com"},"40":{"name":"e04293 - A.M.S.Sumanasooriya","image":"htts://none.com"},"41":{"name":"e04298 - T.A.S.H.Thalangama","image":"htts://none.com"},"42":{"name":"e04299 - M.Thananjeyan","image":"htts://none.com"},"43":{"name":"e04316 - J.A.D.Q.S.Udeshinie","image":"htts://none.com"},"44":{"name":"e04327 - G.L.W.M.A.Welegamage","image":"htts://none.com"},"45":{"name":"e04333 - W.E.S.Wiharagoda","image":"htts://none.com"},"46":{"name":"e04339 - K.A.R.S.Wimalarathne","image":"htts://none.com"},"47":{"name":"e04347 - H.G.P.S.Kulathilaka","image":"htts://none.com"}}

"""

data = json.loads(outputFromJavaScript)
outputJSON = {}

for i in range(len(data)):
    name = data[str(i)]["name"]
    batch = int(name[1:3])
    regNo = int(name[3:6])
    url = data[str(i)]["image"]
    name = name.split("-")[1].strip()
    print(name, batch, regNo, url)
    image_path = f"images/students/e{str(batch).zfill(2)}/e{str(batch).zfill(2)}{str(regNo).zfill(3)}.jpg"
    try:
        urllib.request.urlretrieve(url, "../"+image_path)
    except:
        image_path = "images/students/default.jpg"
    outputJSON[str(f"E/{str(batch).zfill(2)}/{str(regNo).zfill(3)}")] = {"reg_no": f"E/{str(batch).zfill(2)}/{str(regNo).zfill(3)}",
                                                                         "name_with_initials": name,
                                                                         "image_url": image_path}


outputJSONFile = open(f"../_data/stud/e{str(batch).zfill(2)}.json", "w")
outputJSONFile.write(json.dumps(outputJSON, indent=4))
outputJSONFile.close()
