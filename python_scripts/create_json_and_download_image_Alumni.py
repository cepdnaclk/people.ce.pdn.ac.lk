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
{"0":{"name":"e05008 - D.M.PAbhayavickrama","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05008.jpg"},"1":{"name":"e05021 - M.A.S.K.M.Arachchi","image":"http://www.ce.pdn.ac.lk/people/images/e05/e05021.jpg"},"2":{"name":"e05025 - G.Arulananthan","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05025.jpg"},"3":{"name":"e05036 - C.R.W.Basnayaka","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05036.jpg"},"4":{"name":"e05042 - W.R.W.M.Y.S.B.Bulumulla","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05042.jpg"},"5":{"name":"e05049 - R.W.V.P.Chathrangani","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05049.jpg"},"6":{"name":"e05050 - N.W.U.D.Chathurani","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05050.jpg"},"7":{"name":"e05052 - W.I.U.Cooray","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05052.jpg"},"8":{"name":"e05057 - C.K.M.S.Dasunpriya","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05057.jpg"},"9":{"name":"e05062 - M.S.P.De Silva","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05062.jpg"},"10":{"name":"e05074 - H.G.C.Dilrukshi","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05074.jpg"},"11":{"name":"e05075 - S.D.D.Dilrukshi","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05075.jpg"},"12":{"name":"e05076 - D.P.Diluxan","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05076.jpg"},"13":{"name":"e05081 - D.M.S.W.Dissanayake","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05081.jpg"},"14":{"name":"e05087 - E.S.L.Edirisinghe","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05087.jpg"},"15":{"name":"e05089 - E.M.C.B.Ekanayake","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05089.jpg"},"16":{"name":"e05090 - E.M.G.K.Ekanayake","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05090.jpg"},"17":{"name":"e05091 - E.M.P.T.Ekanayake","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05091.jpg"},"18":{"name":"e05093 - M.A.S.Fathima","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05093.jpg"},"19":{"name":"e05095 - W.J.N.Fernando","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05095.jpg"},"20":{"name":"e05099 - A.G.K.M.C.P.Gamakumara","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05099.jpg"},"21":{"name":"e05107 - H.W.S.R.B.Gunathilaka","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05107.jpg"},"22":{"name":"e05108 - T.S.A.Gunawardena","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05108.jpg"},"23":{"name":"e05126 - K.I.P.Jayamini","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05126.jpg"},"24":{"name":"e05129 - J.A.D.N.Jayasinghe","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05129.jpg"},"25":{"name":"e05132 - N.N.Jayasundara","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05132.jpg"},"26":{"name":"e05136 - N.R.E.Jayasuriya","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05136.jpg"},"27":{"name":"e05138 - K.E.I.Jayathissa","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05138.jpg"},"28":{"name":"e05144 - W.S.N.Jayawickrama","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05144.jpg"},"29":{"name":"e05157 - A.A.P.S.Karunarathna","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05157.jpg"},"30":{"name":"e05178 - A.D.K.S.Kumari","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05178.jpg"},"31":{"name":"e05186 - M.P.Lokuhetti","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05186.jpg"},"32":{"name":"e05188 - M.K.S.Madushika","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05188.jpg"},"33":{"name":"e05190 - S.R.B.Malalgoda","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05190.jpg"},"34":{"name":"e05193 - R.M.K.Manjula","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05193.jpg"},"35":{"name":"e05207 - G.M.V.Nawarathne","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05207.jpg"},"36":{"name":"e05212 - P.H.C.Nissanka","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05212.jpg"},"37":{"name":"e05214 - A.A.A.Padmakumara","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05214.jpg"},"38":{"name":"e05222 - W.P.N.Pathirana","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05222.jpg"},"39":{"name":"e05249 - R.M.S.K.D.Rathnayaka","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05249.jpg"},"40":{"name":"e05252 - M.Ratnasabapathipillai","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05252.jpg"},"41":{"name":"e05253 - C.R.M.Ratnasinghe","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05253.jpg"},"42":{"name":"e05265 - N.T.M.Sajith","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05265.jpg"},"43":{"name":"e05267 - K.S.P.S.T.C.Samarasinghe","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05267.jpg"},"44":{"name":"e05268 - G.H.M.M.P.Samaraweera","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05268.jpg"},"45":{"name":"e05270 - D.R.Sampath","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05270.jpg"},"46":{"name":"e05288 - K.C.J.Silva","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05288.jpg"},"47":{"name":"e05290 - S.A.S.I.Silva","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05290.jpg"},"48":{"name":"e05291 - Y.C.P.Silva","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05291.jpg"},"49":{"name":"e05302 - N.A.N.Sugandanee","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05302.jpg"},"50":{"name":"e05311 - W.K.Tharaka","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05311.jpg"},"51":{"name":"e05314 - M.H.F.Thasnim","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05314.jpg"},"52":{"name":"e05319 - R.D.J.S.Thilakarathna","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05319.jpg"},"53":{"name":"e05325 - A.M.B.Uduwerella","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05325.jpg"},"54":{"name":"e05330 - W.M.D.K.Warnasooriya","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05330.jpg"},"55":{"name":"e05333 - P.K.U.R.Weerasena","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05333.jpg"},"56":{"name":"e05334 - W.C.N.Weerasinghe","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e05/e05334.jpg"},"57":{"name":"e05364 - K.P.K.C.Kaluthanthri","image":"http://www.ce.pdn.ac.lk/people/images/e05/e05364.jpg"},"58":{"name":"e05365 - A.U.P.Athukorala","image":"http://www.ce.pdn.ac.lk/people/images/e05/e05365.jpg"},"59":{"name":"e05372 - I.P.M.Priyangika","image":"http://www.ce.pdn.ac.lk/people/images/e05/e05372.jpg"}}

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
