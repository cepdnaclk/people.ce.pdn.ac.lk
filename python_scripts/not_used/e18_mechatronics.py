## Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk
import urllib.request
co224All = """E/18/009 ABEYWEERA P.S. MISS	Student	No groups	20 mins 36 secs
E/18/010 ABEYWICKRAMA A.K.D.A.S. MISS	Student	No groups	7 hours 53 mins
E/18/013 ABILASH R. MR	Student	No groups	2 days 6 hours
E/18/014 AHAMAD I.L.A. MR	Student	No groups	1 hour 36 mins
E/18/017 AARAH J.F. MISS	Student	No groups	3 hours 54 mins
E/18/022 AMARASINGHE D.I. MR	Student	No groups	27 mins 29 secs
E/18/028 ARIYAWANSHA P.H.J.U. MR	Student	No groups	3 hours 1 min
E/18/030 ATHTHANAYAKA A.M.S. MISS	Student	No groups	6 hours 52 mins
E/18/036 BANDARA L.R.M.U. MR	Student	No groups	11 hours 58 mins
E/18/058 DE ALWIS K.K.M. MISS	Student	No groups	1 day 4 hours
E/18/063 DEDIGAMUWA N.T. MR	Student	No groups	1 day 1 hour
E/18/068 DEVINDA G.C. MR	Student	No groups	19 mins
E/18/073 DHANANJAYA W.M.T. MR	Student	No groups	9 mins 5 secs
E/18/077 DHARMARATHNE N.S. MR	Student	No groups	2 hours 42 mins
E/18/097 ESWARAN M. MISS	Student	No groups	4 hours 24 mins
E/18/098 FERNANDO K.A.I. MR	Student	No groups	26 secs
E/18/100 FERNANDO K.N.A. MR	Student	No groups	6 hours 20 mins
E/18/115 GOWSIGAN A. MR	Student	No groups	11 mins
E/18/118 GUNARATHNA H.P.H.M. MR	Student	No groups	1 hour 42 mins
E/18/126 GURUSINGHE D.C. MR	Student	No groups	6 hours 54 mins
E/18/128 HARIHARAN R. MR	Student	No groups	7 hours 4 mins
E/18/131 HEMACHANDRA K.T.H. MR	Student	No groups	18 mins 45 secs
E/18/147 JAMEEL S. MISS	Student	No groups	6 hours 16 mins
E/18/149 JAYAKODY J.M.I.H. MR	Student	No groups	7 hours 37 mins
E/18/150 JAYARATHNA H.M.Y.S. MR	Student	No groups	1 day 19 hours
E/18/154 JAYASUMANA C.H. MISS	Student	No groups	4 hours 28 mins
E/18/155 JAYASUNDARA J.W.K.R.B. MR	Student	No groups	20 hours 5 mins
E/18/156 JAYATHILAKE W.A.T.N. MISS	Student	No groups	1 hour 17 mins
E/18/168 KARAN R. MR	Student	No groups	46 mins 50 secs
E/18/170 KARUNARATHNA W.K. MR	Student	No groups	59 secs
E/18/173 KASTHURIPITIYA K.A.I.M. MR	Student	No groups	1 hour 21 mins
E/18/177 KHAN A.K.M.S. MR	Student	No groups	19 mins 15 secs
E/18/178 KITHMAL P.G.S. MR	Student	No groups	16 hours 30 mins
E/18/180 KODITUWAKKU M.K.N.M. MR	Student	No groups	7 hours 2 mins
E/18/181 KONARA K.M.S.L. MR	Student	No groups	26 mins 44 secs
E/18/203 MADHUSANKA K.G.A.S. MR	Student	No groups	1 hour 45 mins
E/18/214 MANAHARA H.K. MR	Student	No groups	34 mins 39 secs
E/18/224 MIHIRANGA G.D.R. MR	Student	No groups	8 hours 23 mins
E/18/227 MUDALIGE D.H. MR	Student	No groups	27 mins 15 secs
E/18/230 MUNATHANTHRI M.D.H.I. MR	Student	No groups	1 min 40 secs
E/18/242 NIMNADI J.A.S. MISS	Student	No groups	6 days 8 hours
E/18/245 NISHANI K. MISS	Student	No groups	2 days
E/18/264 PRASANNA N.W.G.L.M. MR	Student	No groups	1 day
E/18/266 PREMATHILAKA K.N.I. MR	Student	No groups	12 hours 9 mins
E/18/276 RAJASOORIYA J.M. MR	Student	No groups	1 hour 24 mins
E/18/282 RANASINGHE R.A.N.S. MISS	Student	No groups	8 hours 14 mins
E/18/283 RANASINGHE R.D.J.M. MISS	Student	No groups	12 hours 20 mins
E/18/285 RANASINGHE S.M.T.S.C. MR	Student	No groups	7 mins 51 secs
E/18/297 RATHNAYAKE R.M.P.P. MR	Student	No groups	2 hours 14 mins
E/18/304 RISHAD N.M. MR	Student	No groups	3 hours 44 mins
E/18/316 SANDARUWAN V.B. MR	Student	No groups	23 hours 17 mins
E/18/318 SANDUNIKA S.A.P. MISS	Student	No groups	2 hours 45 mins
E/18/323 SEEKKUBADU H.D. MISS	Student	No groups	5 hours 51 mins
E/18/327 SENEVIRATHNA M.D.C.D. MR	Student	No groups	8 hours 46 mins
E/18/329 SEWWANDI D.W.S.N. MISS	Student	No groups	35 mins 40 secs
E/18/330 SEWWANDI H.R. MISS	Student	No groups	1 hour 58 mins
E/18/340 SUBRAMANIEAM V. MISS	Student	No groups	1 min 52 secs
E/18/349 THALISHA W.G.A.P. MR	Student	No groups	58 mins 27 secs
E/18/354 THARAKA K.K.D.R. MR	Student	No groups	6 hours 8 mins
E/18/366 THULASIYAN Y. MR	Student	No groups	1 hour 41 mins
E/18/368 UDUWANAGE H.U. MR	Student	No groups	4 mins 25 secs
E/18/373 VILAKSHAN V. MR	Student	No groups	11 days 10 hours
E/18/375 VINDULA K.P.A. MR	Student	No groups	7 hours 33 mins
E/18/379 WANDURAGALA T.D.B. MR	Student	No groups	2 hours 8 mins
E/18/382 WEERARATHNE L.D. MR	Student	No groups	1 hour 42 mins
E/18/397 WIJERATHNE E.S.G. MR	Student	No groups	3 hours 52 mins
E/18/398 WIJERATHNE R.M.N.S. MISS	Student	No groups	4 days 5 hours
E/18/402 WIMALASIRI K.H.C.T. MR	Student	No groups	22 mins 50 secs
E/18/406 ZAMEER M.H.M. MR	Student	No groups	12 days 9 hours
E/18/412 DE SILVA M.S.G.M. MR	Student	No groups	5 hours 8 mins"""


e18_CO = open("../_csv/e18_CO.txt", "r")
CO = []
for thisLine in e18_CO:
    CO.append(thisLine.split()[0])
mechatronic = []
regNoNameDICT = {}
for thisLine in co224All.split("\n"):
    regNoNameDICT[thisLine.split()[0]] = " ".join(thisLine.split()[1:-8])
    if thisLine.split()[0] not in CO:
        mechatronic.append(thisLine.split()[0])

feelsAll = open("../_csv/FEeLS_all.txt")
regNoImageLink = {}
for line in feelsAll:
    regNoImageLink[line.split()[0]] = line.split()[-1]

for each in mechatronic:
    regNo = each[-3:]

    urllib.request.urlretrieve(
        regNoImageLink[each], f"../images/students/e18/e18{regNo}.jpg")
    htmlFile = open(f"../pages/students/e18/e18{regNo}.html", "w")
    text = f"""---
layout: studentDetails
permalink: "/students/e18/{int(regNo):03d}/"
title: Abeywickrama A.K.D.A.S.

reg_no: E/18/{int(regNo):03d}
batch: E18

department: Mechanical
current_affiliation: Department of Mechanical Engineering, University of Peradeniya

full_name: {regNoNameDICT[each].title()}
name_with_initials: {regNoNameDICT[each].title()}
preferred_short_name: {regNoNameDICT[each].title()}
preferred_long_name: #
honorific: #

email_faculty: e18{int(regNo):03d}@eng.pdn.ac.lk
email_personal: #

location: #

url_cv: #
url_website: #
url_linkedin: #
url_github: #
url_facebook: #
url_researchgate: #
url_twitter: #

interests: #

image_url: "images/students/e18/e18{regNo}.jpg"
---
    """
    htmlFile.write(text)
    htmlFile.close()
