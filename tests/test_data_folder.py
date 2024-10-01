# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk
import unittest
# import b_webdriver_functions
# import a_config_test
# import requests
# from selenium.webdriver.common.by import By
import os
import json


class Tests(unittest.TestCase):
    def test_all_jsons_in_data_folder(self):
        allFiles = os.listdir("../_data")
        for eachFile in allFiles:
            if ".json" not in eachFile:
                continue

            try:
                jsonFile = open("../_data/" + eachFile)
                json.load(jsonFile)
                jsonFile.close()
            except:
                self.fail("JSON file " + eachFile + " is not valid")

    def test_all_jsons_in_data_stud_folder(self):
        allFiles = os.listdir("../_data/stud")
        for eachFile in allFiles:
            if ".json" not in eachFile:
                continue

            try:
                jsonFile = open("../_data/stud/" + eachFile)
                json.load(jsonFile)
                jsonFile.close()
            except:
                self.fail("JSON file " + eachFile + " is not valid")


if __name__ == '__main__':
    unittest.main()
