input = """E/02A/002		P.A.C. Abeywicrama		2nd class honours (Upper)
E/02A/004		B.A.S.P. Abeysekara		2nd class honours (Lower)
E/02A/006		M.S.A. Ahamed		1st class honours
E/02A/008		A.D.V. Amarasinghe		2nd class honours (Lower)
E/02A/017		S. Atchuthan		2nd class honours (Lower)
E/02A/027		S.W. Buthpitiya		1st class honours
E/02A/056		G.V.B.N. Galgomuwa		2nd class honours (Upper)
E/02A/093		G.W. Jayarathne		2nd class honours (Lower)
E/02A/109		K. Jeyavani		2nd class honours (Lower)
E/02A/112		V. Kalyani		2nd class honours (Upper)
E/02A/116		C.M. Karunarathna		2nd class honours (Upper)
E/02A/118		G.S.N. Karunarathna		2nd class honours (Upper)
E/02A/124		Y. Kishanthan		2nd class honours (Lower)
E/02A/141		W.A.M. Kusumalatha		2nd class honours (Upper)
E/02A/151		D.M.A.B. Mailewa		2nd class honours (Upper)
E/02A/158		A. Mathanky		2nd class honours (Upper)
E/02A/163		C.A. Munasinghe		1st class honours
E/02A/167		R.T.V. Niroshanie		2nd class honours (Lower)
E/02A/173		H.P.A.I. Pathirana		2nd class honours (Upper)
E/02A/183		M.A.D.C. Premarathna		2nd class honours (Upper)
E/02A/195		R.M.M.B. Rajapakse		2nd class honours (Upper)
E/02A/198		T.D. Rambukwella		2nd class honours (Lower)
E/02A/205		E.S.C. Ranaweera		2nd class honours (Upper)
E/02A/206		W.R.C.I. Ranaweera		2nd class honours (Lower)
E/02A/208		B.M.I.U. Rathnayaka		2nd class honours (Upper)
E/02A/217		S.M. Rinos		2nd class honours (Lower)
E/02A/220		M.H.S.M.I. Sabar		2nd class honours (Upper)
E/02A/223		M.K.A. Samanmalee		2nd class honours (Upper)
E/02A/243		A.L.F. Shanaz		1st class honours
E/02A/251		M.M.D. Sriyananda		2nd class honours (Upper)
E/02A/262		E.H. Thennakoon		2nd class honours (Lower)
E/02A/267		T. Thushyanthi		2nd class honours (Lower)
E/02A/284		T.D.B. Weerasinghe		2nd class honours (Lower)
E/02A/287		C.S. Weliwita		2nd class honours (Lower)
E/02A/288		W.M.U. Wijayasundara		2nd class honours (Lower)
E/02A/293		W.P.D. Wijesinghe		2nd class honours (Lower)
E/02A/296		R.A.N.N. Wijewardana		2nd class honours (Upper)
E/02A/316		M.I.S.S. Abeysinghe		2nd class honours (Lower)
E/02A/320		G.L.I.M.K. Kahanda		1st class honours
E/02A/326		C.B. Hatharaliyadda		1st class honours
E/02/314		U.G. Kanewala		1st class honours"""

inputSplitted = input.split("\n")
outputJSON = {}
for eachLine in inputSplitted:
    data = eachLine.split("\t")
    regNo = data[0]
    name = data[2]
    outputJSON[regNo] = {"reg_no": regNo, "name_with_initials": name,
                         "image_url": "images/students/default.jpg"}

outputFile = open("../_data/stud/e02.json","w")
import json
outputFile.write(json.dumps(outputJSON,indent=4))
outputFile.close()