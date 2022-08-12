# Base functions used by the tests.
# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk

from selenium import webdriver
import a_config_test


# disable the unwanted error msg
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# run headless mode
options.add_argument('--headless')

# ge the driver
driver = webdriver.Chrome("./webdriver/chromedriver.exe", options=options)


def getHomepage():
    driver.get(a_config_test.SERVER_URL)
    return driver


def getSearchByName():
    driver.get(a_config_test.SERVER_URL + "search/by-name/")
    return driver


def getSearchByRegNo():
    driver.get(a_config_test.SERVER_URL + "search/by-reg-no/")
    return driver


def getSearchByCurrAff():
    driver.get(a_config_test.SERVER_URL + "search/by-current-affiliation/")
    return driver


def getSearchByLocation():
    driver.get(a_config_test.SERVER_URL + "search/by-location/")
    return driver


def getSearchByInterestStudent():
    driver.get(a_config_test.SERVER_URL + "search/by-interests/")
    return driver


def getSearchByInterestStaff():
    driver.get(a_config_test.SERVER_URL + "search/by-research-interests/")
    return driver


def getAcademicStaff():
    driver.get(a_config_test.SERVER_URL + "staff/academic/")
    return driver
