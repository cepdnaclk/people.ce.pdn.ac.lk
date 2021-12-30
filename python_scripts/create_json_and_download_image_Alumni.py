# Create json file in _data/stud/*.json + download image using information taken from javascript code
#  https://cepdnaclk.github.io/department-website-2013/people/e08.html
# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk

# run js on site
"""
output = {};
list1 = document.getElementsByTagName("tr");
let count = 0;
for (let i = 0; i < list1.length; i=i+1) {
  output[count] = { name : list1[i].getElementsByTagName("th")[0].innerText , image : list1[i].getElementsByTagName("th")[1].getElementsByTagName("a")[0].href }
  count = count + 1;
  output[count] = { name : list1[i].getElementsByTagName("th")[3].innerText , image : list1[i].getElementsByTagName("th")[4].getElementsByTagName("a")[0].href }
  count = count + 1;
}
JSON.stringify(output)
"""

import urllib.request
import json


# the output,

outputFromJavaScript = """
{"0":{"name":"e08001 - M.F.M. Aadhil","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08001.jpg"},"1":{"name":"e08004 - A.M.M.S. Adhikari","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08004.jpg"},"2":{"name":"e08022 - S. Arudchutha","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08022.jpg"},"3":{"name":"e08030 - A.M.S.B. Baminiwatta","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08030.jpg"},"4":{"name":"e08038 - M.M.P.P. Bandara","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08038.jpg"},"5":{"name":"e08040 - R.S.M.S. Bandara","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08040.jpg"},"6":{"name":"e08053 - D.H.T. Dasanayke","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08053.jpg"},"7":{"name":"e08054 - D.J.E Davidson","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08054.jpg"},"8":{"name":"e08058 - S.H.S.Y. De Silva","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08058.jpg"},"9":{"name":"e08059 - L.S. Devamanthri","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08059.jpg"},"10":{"name":"e08061 - P. Dhanushanath","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08061.jpg"},"11":{"name":"e08065 - M.H.M.G. Dissanayaka","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08065.jpg"},"12":{"name":"e08081 - W.M.KS.D. Fernando","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08081.jpg"},"13":{"name":"e08082 - M.Y.M. Firnas","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08082.jpg"},"14":{"name":"e08086 - D.P.S. Gamachchige","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08086.jpg"},"15":{"name":"e08088 - S. Gobiga","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08088.jpg"},"16":{"name":"e08092 - A.S. Gomez","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08092.jpg"},"17":{"name":"e08098 - W.M.H.D. Gunasiri","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08098.jpg"},"18":{"name":"e08099 - B. Gunenthiran","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08099.jpg"},"19":{"name":"e08109 - H.K.L. Hettiarachchi","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08109.jpg"},"20":{"name":"e08110 - H.B.D. Himali","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08110.jpg"},"21":{"name":"e08130 - S.B. Jayasundara","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08130.jpg"},"22":{"name":"e08131 - W.D.D.N. Jayasundara","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08131.jpg"},"23":{"name":"e08132 - I.R.P.D.I. Jayathilaka","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08132.jpg"},"24":{"name":"e08139 - P.H.P.I. Jayatissa","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08139.jpg"},"25":{"name":"e08145 - C.P.S. Kaluarachchi","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08145.jpg"},"26":{"name":"e08155 - K. Kesikan","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08155.jpg"},"27":{"name":"e08158 - K.A.U.A. Kodithuwakku","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08158.jpg"},"28":{"name":"e08172 - W.H.M.A.U. Kumara","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08172.jpg"},"29":{"name":"e08182 - H.D.S. Lakmali","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08182.jpg"},"30":{"name":"e08187 - D.K.I. Madhushanka","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08187.jpg"},"31":{"name":"e08189 - W.T. Madushan","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08189.jpg"},"32":{"name":"e08190 - M.A.G. Madushanka","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08190.jpg"},"33":{"name":"e08191 - U.D.G.T. Madushanka","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08191.jpg"},"34":{"name":"e08194 - H.M.D.K. Mallikarachchi","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08194.jpg"},"35":{"name":"e08199 - B.S. Manuweera","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08199.jpg"},"36":{"name":"e08221 - L. Niranjan","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08221.jpg"},"37":{"name":"e08228 - T. Nishanthy","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08228.jpg"},"38":{"name":"e08229 - P.H.A. Nissanka","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08229.jpg"},"39":{"name":"e08237 - S.T. Paranagama","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08237.jpg"},"40":{"name":"e08245 - A.L.S.M. Perera","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08245.jpg"},"41":{"name":"e08248 - M.N.T. Perera","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08248.jpg"},"42":{"name":"e08255 - H.M.P. Prasadini","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08255.jpg"},"43":{"name":"e08263 - R.M.D. Rajapaksha","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08263.jpg"},"44":{"name":"e08270 - R.P.A.D. Randeni","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08270.jpg"},"45":{"name":"e08280 - M.C.M. Reejan","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08280.jpg"},"46":{"name":"e08291 - W.M.D. Sajini","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08291.jpg"},"47":{"name":"e08298 - A.P.I.S. Sandaruwan","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08298.jpg"},"48":{"name":"e08305 - M.H. Satheeq","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08305.jpg"},"49":{"name":"e08347 - T.M.G. Tennakoon","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08347.jpg"},"50":{"name":"e08352 - R.M.K.G.C. Thennakoon","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08352.jpg"},"51":{"name":"e08354 - S. Theshoban","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08354.jpg"},"52":{"name":"e08362 - G.A.D.R. Thushara","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08362.jpg"},"53":{"name":"e08373 - S. Vinodharanie","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08373.jpg"},"54":{"name":"e08387 - W.M.M.P.B. Wickramasinghe","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08387.jpg"},"55":{"name":"e08390 - W.G.S. Wiharagoda","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08390.jpg"},"56":{"name":"e08403 - K. Yaathavarajan","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08403.jpg"},"57":{"name":"e08404 - G.K. Yalpathwala","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08404.jpg"},"58":{"name":"e08405 - D.N. Yaparathne","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08405.jpg"},"59":{"name":"e08409 - M.A.M. Ziyam","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e08/e08409.jpg"}}

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
    outputJSON[str(f"E/{str(batch).zfill(2)}/{str(regNo).zfill(3)}")] = {"reg_no": f"E/{str(batch).zfill(2)}/{str(regNo).zfill(3)}",
                                                                         "name_with_initials": name,
                                                                         "image_url": image_path}
    urllib.request.urlretrieve(url, "../"+image_path)


outputJSONFile = open(f"../_data/stud/e{str(batch).zfill(2)}.json", "w")
outputJSONFile.write(json.dumps(outputJSON, indent=4))
outputJSONFile.close()
