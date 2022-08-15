# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk
import unittest
import b_webdriver_functions
import a_config_test
from selenium.webdriver.common.by import By


class Tests(unittest.TestCase):
    def test_if_search_shows_Roshan(self):
        driver = b_webdriver_functions.getHomepage()
        driver.find_element(by=By.ID, value="search-input").send_keys("Roshan")
        homeButton = driver.find_element(by=By.LINK_TEXT, value="Prof. Roshan G. Ragel")
        link = homeButton.get_attribute("href")
        self.assertEqual(link,  a_config_test.SERVER_URL + "staff/academic/roshan-ragel/", "Search doesnt show Roshan")

    def test_if_search_shows_Ishan(self):
        driver = b_webdriver_functions.getHomepage()
        driver.find_element(by=By.ID, value="search-input").send_keys("E18098")
        homeButton = driver.find_element(by=By.LINK_TEXT, value="Kurukulasuriya Anton Ishan Fernando - E/18/098")
        link = homeButton.get_attribute("href")
        self.assertEqual(link,  a_config_test.SERVER_URL + "students/e18/098/", "Search doesnt show Ishan")

    def test_if_search_shows_documentation(self):
        driver = b_webdriver_functions.getHomepage()
        driver.find_element(by=By.ID, value="search-input").send_keys("how to")
        homeButton = driver.find_element(by=By.LINK_TEXT, value="How to add a new Student Profile page?")
        link = homeButton.get_attribute("href")
        self.assertEqual(link,  a_config_test.SERVER_URL + "documentation/add-student-page/", "Search doesnt show documentation")

    def test_if_search_shows_student_without_profile_page(self):
        driver = b_webdriver_functions.getHomepage()
        driver.find_element(by=By.ID, value="search-input").send_keys("E/00/039")
        homeButton = driver.find_element(by=By.LINK_TEXT, value="CHANAKA M.H. - E/00/039")
        link = homeButton.get_attribute("href")
        self.assertEqual(link,  a_config_test.SERVER_URL + "students/e00/", "Search doesnt show profiles without profile page")

    def test_if_search_shows_non_academic_staff(self):
        driver = b_webdriver_functions.getHomepage()
        driver.find_element(by=By.ID, value="search-input").send_keys("Priyangani Samaratunge")
        homeButton = driver.find_element(by=By.LINK_TEXT, value="Priyangani Samaratunge - Non-Academic Staff")
        link = homeButton.get_attribute("href")
        self.assertEqual(link,  a_config_test.SERVER_URL + "staff/non-academic-staff/", "Search doesnt show Non Academic Staff")

    def test_if_search_shows_temporary_academic_staff(self):
        driver = b_webdriver_functions.getHomepage()
        driver.find_element(by=By.ID, value="search-input").send_keys("Nuwan Jaliyagoda")
        homeButton = driver.find_element(by=By.LINK_TEXT, value="Nuwan Jaliyagoda - Temporary Academic Staff")
        link = homeButton.get_attribute("href")
        self.assertEqual(link,  a_config_test.SERVER_URL + "staff/temporary-academic-staff/", "Search doesnt show temp academic staff")

    def test_if_search_shows_past_heads(self):
        driver = b_webdriver_functions.getHomepage()
        driver.find_element(by=By.ID, value="search-input").send_keys("Prof Noel Fernando")
        homeButton = driver.find_element(by=By.LINK_TEXT, value="Prof Noel Fernando - Past Heads of the Department")
        link = homeButton.get_attribute("href")
        self.assertEqual(link,  a_config_test.SERVER_URL + "staff/past-heads-of-dep/", "Search doesnt show temp academic staff")

    def test_advanced_search_by_name(self):
        driver = b_webdriver_functions.getHomepage()
        link = driver.find_element(by=By.ID, value="byName").get_attribute("href")
        self.assertEqual(link, a_config_test.SERVER_URL + "search/by-name/", "Search by name link is not correct")

    def test_advanced_search_by_regNO(self):
        driver = b_webdriver_functions.getHomepage()
        link = driver.find_element(by=By.ID, value="byRegNo").get_attribute("href")
        self.assertEqual(link, a_config_test.SERVER_URL + "search/by-reg-no/", "Search by reg no link is not correct")

    def test_advanced_search_by_curr_aff(self):
        driver = b_webdriver_functions.getHomepage()
        link = driver.find_element(by=By.ID, value="byCurrAff").get_attribute("href")
        self.assertEqual(link, a_config_test.SERVER_URL + "search/by-current-affiliation/", "Search by curr aff link is not correct")

    def test_advanced_search_by_location(self):
        driver = b_webdriver_functions.getHomepage()
        link = driver.find_element(by=By.ID, value="byLocation").get_attribute("href")
        self.assertEqual(link, a_config_test.SERVER_URL + "search/by-location/", "Search by location link is not correct")

    def test_advanced_search_by__interest_stud(self):
        driver = b_webdriver_functions.getHomepage()
        link = driver.find_element(by=By.ID, value="byInterestStud").get_attribute("href")
        self.assertEqual(link, a_config_test.SERVER_URL + "search/by-interests/", "Search by name interest stud is not correct")

    def test_advanced_search_by_interest_staff(self):
        driver = b_webdriver_functions.getHomepage()
        link = driver.find_element(by=By.ID, value="byInterestStaff").get_attribute("href")
        self.assertEqual(link, a_config_test.SERVER_URL + "search/by-research-interests/", "Search by interest staff link is not correct")

    def test_search_shows_at_least_one_student_from_each_batch(self):
        driver = b_webdriver_functions.getHomepage()
        batchNumber = list(range(00, 20))
        batchNumber.append(99)
        batchNumber.append(98)
        for batch in batchNumber:
            # print(batch)
            driver.find_element(by=By.ID, value="search-input").send_keys(f"E{batch:02d}")
            homeButton = driver.find_element(By.XPATH, value="//*[@class='list-group-item list-group-item-action' or @class='jsb']")
            link = homeButton.get_attribute("href")
            flag = link.find(f"e{batch:02d}")
            self.assertTrue(flag, "Search doesnt have one batch")
            driver.find_element(by=By.ID, value="search-input").clear()


if __name__ == '__main__':
    unittest.main()
