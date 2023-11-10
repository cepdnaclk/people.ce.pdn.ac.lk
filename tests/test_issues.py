# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk
import unittest
import b_webdriver_functions
import a_config_test
from selenium.webdriver.common.by import By
import requests
import os


class Tests(unittest.TestCase):
    def test_E19_have_mechanical_students(self):
        driver = b_webdriver_functions.getURL("students/e19/")
        if (
            "External Students - Department of Mechanical Engineering"
            not in driver.page_source
        ):
            self.fail("E19 doesnt have mechanical students")

    def test_E18_have_mechanical_students(self):
        driver = b_webdriver_functions.getURL("students/e18/")
        if (
            "External Students - Department of Mechanical Engineering"
            not in driver.page_source
        ):
            self.fail("E18 deosnt have mechanical students")

    def test_E17_doesnt_have_mechanical_students(self):
        driver = b_webdriver_functions.getURL("students/e17/")
        if (
            "External Students - Department of Mechanical Engineering"
            not in driver.page_source
        ):
            self.fail("E17 doesnt have mechanical students")

    def test_All_students_external_urls_have_http_or_https(self):
        # the links doesnt work if they dont have the http prefix

        studentsFolder = "../pages/students"
        for eachFolder in os.listdir(studentsFolder):
            # e18 e19 etc

            # skip the html files and the indexPages folder
            if "indexPages" in eachFolder or ".html" in eachFolder:
                continue

            for eachStudent in os.listdir(studentsFolder + "/" + eachFolder + "/"):
                # e18098.html e18xxx.html files
                filePath = studentsFolder + "/" + eachFolder + "/" + eachStudent

                with open(filePath, "r") as f:
                    # inside of each file

                    for eachLine in f:
                        if "url_" in eachLine:
                            splitted = eachLine.split()

                            # skip if the url is empty
                            if len(splitted) == 1 or splitted[1] == "#":
                                continue

                            # check for http
                            if "http" not in splitted[1] or "://" not in splitted[1]:
                                self.fail(
                                    "URL in " + filePath + " does not contain http"
                                )


if __name__ == "__main__":
    unittest.main()
