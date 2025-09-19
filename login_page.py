"""Page Object Model - Login page of Guvi.
It has locators of elements and actions on that page"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class Login_guvi():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)
        # Locator of elements
        self.email_locator = (By.ID, 'email')
        self.password_locator = (By.ID,'password')
        self.login_button_locator = (By.CLASS_NAME,'login-btn')
        self.error_message_email_locator = (By.XPATH,'// *[ @ id = "emailgroup"] / div')
        self.error_message_password_locator = (By.XPATH,'// *[ @ id = "passwordGroup"] / div')

    # To enter email
    def enter_email(self,email):
        self.wait.until(ec.visibility_of_element_located(self.email_locator)).clear()
        self.driver.find_element(*self.email_locator).send_keys(email)

    # To enter password
    def enter_password(self,password):
        self.wait.until(ec.visibility_of_element_located(self.password_locator)).clear()
        self.driver.find_element(*self.password_locator).send_keys(password)

    # To click Login
    def click_login_button(self):
        try:
            self.wait.until(ec.presence_of_element_located(self.login_button_locator))
            self.driver.find_element(*self.login_button_locator).click()
        except Exception as e:
            print(f"Exception: {e}")
            return None

    # To get error message when invalid username or password entered
    def get_error_message(self):
        try:
            incorrect_email=self.wait.until(ec.visibility_of_element_located(self.error_message_email_locator))
            incorrect_password =self.wait.until(ec.visibility_of_element_located(self.error_message_password_locator))
            if incorrect_email:
                error_msg = self.driver.find_element(*self.error_message_email_locator).text
            elif incorrect_password:
                error_msg = self.driver.find_element(*self.error_message_password_locator).text
            return error_msg
        except Exception as e:
            print(f"Exception: {e}")
            return None

