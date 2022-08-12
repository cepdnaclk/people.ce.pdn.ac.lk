import unittest
import webdriver_functions
import a_config_test
from selenium.webdriver.common.by import By


class Tests(unittest.TestCase):
    
    # Used to test if the advanced search jsons are valid and site shows results
    def test_page_loads(self):
        driver = webdriver_functions.getSearchByName()
        self.assertTrue(driver.find_element(by=By.ID, value="search-input").is_displayed(), "Search by name page did not load")

    def test_shows_roshan(self):
        driver = webdriver_functions.getSearchByName()
        driver.find_element(by=By.ID, value="search-input").send_keys("Roshan")
        link = driver.find_element(by=By.LINK_TEXT, value="Prof. Roshan G. Ragel").get_attribute("href")
        self.assertEqual(link, a_config_test.SERVER_URL + "staff/academic/roshan-ragel/", "Roshan Ragel link in search by name is wrong")

    def test_reg_no_shows_Ishan(self):
        driver = webdriver_functions.getSearchByRegNo()
        driver.find_element(by=By.ID, value="search-input").send_keys("E18098")
        link = driver.find_element(by=By.LINK_TEXT, value="Kurukulasuriya Anton Ishan Fernando - E/18/098").get_attribute("href")
        self.assertEqual(link, a_config_test.SERVER_URL + "students/e18/098/", "Ishan link in search by reg no is wrong")

    def test_curr_aff_shows_results(self):
        driver = webdriver_functions.getSearchByCurrAff()
        driver.find_element(by=By.ID, value="search-input").send_keys("wso2")
        link = driver.find_element(by=By.LINK_TEXT, value="Sanjeewa R. B. Malalgoda - E/05/190").get_attribute("href")
        self.assertEqual(link, a_config_test.SERVER_URL + "students/e05/190/", "Search by curr aff is wrong")

    def test_by_location(self):
        driver = webdriver_functions.getSearchByLocation()
        driver.find_element(by=By.ID, value="search-input").send_keys("Negombo")
        link = driver.find_element(by=By.LINK_TEXT, value="Kurukulasuriya Anton Ishan Fernando - E/18/098").get_attribute("href")
        self.assertEqual(link, a_config_test.SERVER_URL + "students/e18/098/", "Search by lcoation is wrong")

    def test_by_interest_student(self):
        driver = webdriver_functions.getSearchByInterestStudent()
        driver.find_element(by=By.ID, value="search-input").send_keys("art")
        link = driver.find_element(by=By.LINK_TEXT, value="Dhammika Marasinghe - E/11/258").get_attribute("href")
        self.assertEqual(link, a_config_test.SERVER_URL + "students/e11/258/", "Search by interest student is wrong")

    def test_by_interest_staff(self):
        driver = webdriver_functions.getSearchByInterestStaff()
        driver.find_element(by=By.ID, value="search-input").send_keys("machine learning")
        link = driver.find_element(by=By.LINK_TEXT, value="Mr. Amila Indika").get_attribute("href")
        self.assertEqual(link, a_config_test.SERVER_URL + "staff/academic/amila-indika/", "Search by interest staff is wrong")


if __name__ == '__main__':
    unittest.main()
