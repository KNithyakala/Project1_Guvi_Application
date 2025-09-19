"""Page Object Model - Dashboard page of Guvi.
It has locators of elements and actions on that page"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class Dashboard_guvi():
    def __init__(self,driver):
        # driver and wait variable creation
        self.driver = driver
        self.wait = WebDriverWait(driver,40)
        # locator of elements
        self.profile_name_locator = (By.XPATH,'//h1[@class="greet-user userName"]')
        self.profile_locator       = (By.XPATH,'//*[@id="accountGroup"]/button')
        self.sign_out_locator      = (By.ID, 'signout')

    # To get the welcome message on that page
    def welcome_message(self):
        self.wait.until(ec.visibility_of_element_located(self.profile_name_locator))

    # Logout
    def logout(self):
        self.wait.until(ec.visibility_of_element_located(self.profile_locator)).click()
        self.wait.until(ec.visibility_of_element_located(self.sign_out_locator)).click()