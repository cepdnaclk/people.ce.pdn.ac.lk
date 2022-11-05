# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk
from dataclasses import replace
import unittest
import b_webdriver_functions
import a_config_test
from selenium.webdriver.common.by import By
import requests


class Tests(unittest.TestCase):
    def test_loads_page(self):
        driver = b_webdriver_functions.getDocumentation()
        if driver.page_source.find("Documentation") == -1:
            self.fail("Documentation page did not load")

    def test_every_link_in_page(self):
        driver = b_webdriver_functions.getDocumentation()
        elems = driver.find_elements(by=By.XPATH, value="//a[@href]")
       # print("Number of links: " + str(len(elems)))
        for elem in elems:
            link = elem.get_attribute("href")
            if a_config_test.SERVER_URL not in link:
                # dont have to test external links
                continue
            thisRequest = requests.get(link)
            self.assertTrue(thisRequest.status_code == 200, link + " is not valid")

    def test_every_link_in_each_documentation_page(self):
        driver = b_webdriver_functions.getDocumentation()
        elems = driver.find_elements(by=By.XPATH, value="//a[@href]")
        links = []
        for elem in elems:
            link = elem.get_attribute("href")
            if link.find("documentation") < 0:
                # dont have to test external links
                continue
            links.append(link)
        for eachLink in links:
            if eachLink.find("#") > 0:
                continue
            eachLink = eachLink.replace(a_config_test.SERVER_URL, "")
            driver = b_webdriver_functions.getURL(eachLink)
            elems = driver.find_elements(by=By.XPATH, value="//a[@href]")
            # print(f"{eachLink} Number of links: " + str(len(elems)))

            for elem in elems:
                link = elem.get_attribute("href")
                if a_config_test.SERVER_URL not in link:  # if this is an external link dont test
                    continue
                thisRequest = requests.get(link)
                # print(link)
                self.assertTrue(thisRequest.status_code == 200, link + " is not valid")


if __name__ == '__main__':
    unittest.main()
