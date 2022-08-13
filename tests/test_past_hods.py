# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk
import unittest
import b_webdriver_functions
import a_config_test
import requests
from selenium.webdriver.common.by import By
import json


class Tests(unittest.TestCase):
    def test_if_page_loads(self):
        driver = b_webdriver_functions.getPastHoDs()
        if driver.page_source.find("Past Heads of the Department") == -1:
            self.fail("Past HoDs page did not load")

    def test_every_link_in_page(self):
        driver = b_webdriver_functions.getPastHoDs()
        elems = driver.find_elements(by=By.XPATH, value="//a[@href]")
       # print("Number of links: " + str(len(elems)))
        for elem in elems:
            link = elem.get_attribute("href")
            if a_config_test.SERVER_URL not in link:
                # dont have to test external links
                continue
            thisRequest = requests.get(link)
            self.assertTrue(thisRequest.status_code == 200, link + " is not valid")

    def test_check_if_all_staff_are_shown(self):
        staffFile = open("../_data/past_heads_of_dep.json")
        jsonObject = json.load(staffFile)
        staffFile.close()

        driver = b_webdriver_functions.getPastHoDs()
        for eachStaff in jsonObject:
            if driver.page_source.find(eachStaff["staff_name"]) == -1:
                self.fail(eachStaff["staff_name"] + " was not found")


if __name__ == '__main__':
    unittest.main()
