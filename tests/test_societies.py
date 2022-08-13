# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk
import unittest
# import b_webdriver_functions
# import a_config_test
# import requests
# from selenium.webdriver.common.by import By
import os
import json


class Tests(unittest.TestCase):
    def test_all_jsons_in_societies_folder(self):
        allFiles = os.listdir("../societies")
        for eachFile in allFiles:
            if ".json" not in eachFile:
                continue

            try:
                jsonFile = open("../societies/" + eachFile)
                json.load(jsonFile)
                jsonFile.close()
            except:
                self.fail("JSON file " + eachFile + " is not valid")


if __name__ == '__main__':
    unittest.main()
