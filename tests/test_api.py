# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk
from lib2to3.pgen2 import driver
import unittest
import b_webdriver_functions
import a_config_test
from selenium.webdriver.common.by import By
import json


class Tests(unittest.TestCase):
    def test_if_Staff_API_has_valid_syntax(self):
        driver = b_webdriver_functions.getStaffAPI()
        jsonString = driver.execute_script("return document.body.innerText")
        try:
            json.loads(jsonString)
        except:
            self.fail("Staff API is not valid")

    def test_if_Student_API_has_valid_syntax(self):
        driver = b_webdriver_functions.getStudentAPI()
        jsonString = driver.execute_script("return document.body.innerText")
        try:
            json.loads(jsonString)
        except:
            self.fail("Stduent API is not valid")


if __name__ == '__main__':
    unittest.main()
