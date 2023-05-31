# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk
import unittest
import b_webdriver_functions
import a_config_test
import requests
from selenium.webdriver.common.by import By
import os
import json


class Tests(unittest.TestCase):
    def test_badges_folder_jsons(self):
        for eachFile in ['casual_instructors_2021.json', 'web_team.json']:
            try:
                jsonFile = open("../badges/" + eachFile)
                json.load(jsonFile)
                jsonFile.close()
            except:
                self.fail("JSON file " + eachFile + " is not valid")

    def test_if_badge_exists_in_student_profile_page(self):
        driver = b_webdriver_functions.getURL("students/e18/100/")
        badgeTitle = driver.find_element(By.CLASS_NAME, value="badge-image").get_attribute('alt')
        self.assertTrue("Web Consultation Team" in badgeTitle, "Badge is not shown in E/18/100")


if __name__ == '__main__':
    unittest.main()
