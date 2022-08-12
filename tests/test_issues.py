import unittest
import webdriver_functions
import a_config_test
from selenium.webdriver.common.by import By
import requests


class Tests(unittest.TestCase):
    def test_E19_doesnt_have_mechanical_students(self):
        driver = webdriver_functions.getURL("students/e19/")
        if "External Students - Department of Mechanical Engineering" in driver.page_source:
            self.fail("E19 has mechanical students")

    def test_E18_have_mechanical_students(self):
        driver = webdriver_functions.getURL("students/e18/")
        if "External Students - Department of Mechanical Engineering" not in driver.page_source:
            self.fail("E18 deosnt have mechanical students")

    def test_E17_doesnt_have_mechanical_students(self):
        driver = webdriver_functions.getURL("students/e17/")
        if "External Students - Department of Mechanical Engineering" not in driver.page_source:
            self.fail("E17 doesnt have mechanical students")


if __name__ == '__main__':
    unittest.main()
