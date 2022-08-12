import unittest
import webdriver_functions
import a_config_test
import requests
import json
from selenium.webdriver.common.by import By


class Tests(unittest.TestCase):
    def test_if_student_pages_load(self):
        file1 = open("../_data/students.json")
        jsonObject = json.load(file1)
        file1.close()
        for each in jsonObject:
            url = each["url"]
            self.assertTrue(requests.get(a_config_test.SERVER_URL + url).status_code == 200, url + " is not valid")

            driver = webdriver_functions.getURL(url)
            elems = driver.find_elements(by=By.XPATH, value="//a[@href]")
            # print("test_if_student_pages_load Number of links: " + str(len(elems)))
            for elem in elems:
                link = elem.get_attribute("href")
                if a_config_test.SERVER_URL not in link:
                    # dont have to test external links
                    continue
                thisRequest = requests.get(link)
                self.assertTrue(thisRequest.status_code == 200, link + " is not valid")

    def test_alumni_pages(self):
        for each in range(15, -1, -1):
            url = f"students/e{each:02d}/"
            # print(url)
            self.assertTrue(requests.get(a_config_test.SERVER_URL + url).status_code == 200, url + " is not valid")

            driver = webdriver_functions.getURL(url)
            elems = driver.find_elements(by=By.XPATH, value="//a[@href]")
            # print("test_alumni_pages Number of links: " + str(len(elems)))
            for elem in elems:
                link = elem.get_attribute("href")
                if a_config_test.SERVER_URL not in link:
                    # dont have to test external links
                    continue
                thisRequest = requests.get(link)
                self.assertTrue(thisRequest.status_code == 200, link + " is not valid")

    def test_alumni_pages_e02a_and_99_98(self):
        for each in ["02a", "99", "98"]:
            url = f"students/e{each}/"
            # print(url)
            self.assertTrue(requests.get(a_config_test.SERVER_URL + url).status_code == 200, url + " is not valid")

            driver = webdriver_functions.getURL(url)
            elems = driver.find_elements(by=By.XPATH, value="//a[@href]")
            # print("test_alumni_pages_e02a_and_99_98 Number of links: " + str(len(elems)))
            for elem in elems:
                link = elem.get_attribute("href")
                if a_config_test.SERVER_URL not in link:
                    # dont have to test external links
                    continue
                thisRequest = requests.get(link)
                self.assertTrue(thisRequest.status_code == 200, link + " is not valid")


if __name__ == '__main__':
    unittest.main()
