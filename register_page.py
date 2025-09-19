"""Page Object Model - Register page of Guvi.
It has locators of elements and actions on that page"""


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

class Register_guvi():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)
        # Locators of elements
        self.name            = (By.ID,"name")
        self.email           = (By.ID,"email")
        self.password        = (By.ID,"password")
        self.mobile_number   = (By.ID,"mobileNumber")
        self.signup_button   = (By.ID,"signup-btn")
        self.current_profile = (By.ID,"profileDrpDwn")
        self.degree          = (By.ID,"degreeDrpDwn")
        self.year_pass_out   = (By.ID,"year")
        self.submit_button   = (By.ID,"details-btn")
        self.login_link      = (By.XPATH,'//a[@class="login"]')

    # Fill up the register page
    def enter_details(self):
        self.wait.until(ec.visibility_of_element_located(self.name)).send_keys("Nithya")
        self.wait.until(ec.visibility_of_element_located(self.email)).send_keys("nk7@gmail.com")
        self.wait.until(ec.visibility_of_element_located(self.password)).send_keys("Bnrh@1234")
        self.wait.until(ec.visibility_of_element_located(self.mobile_number)).send_keys("1234567890")
        self.driver.find_element(*self.signup_button).click()
        self.wait.until(ec.visibility_of_element_located(self.current_profile))
        current_profile= self.driver.find_element(*self.current_profile)
        select_dropdown = Select(current_profile)
        select_dropdown.select_by_visible_text("Working professional in Non-IT")
        degree = self.driver.find_element(*self.degree)
        select_dropdown = Select(degree)
        select_dropdown.select_by_visible_text("B.Sc. / M.Sc.")
        self.wait.until(ec.visibility_of_element_located(self.year_pass_out)).send_keys("2005")
        self.wait.until(ec.visibility_of_element_located(self.submit_button)).click()

    # To navigate to Login page from Register page
    def click_login_link(self):
        self.driver.find_element(*self.login_link).click()