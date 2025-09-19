"""Page Object Model - Home page of Guvi.
It has locators of elements and actions on that page"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Homepage_guvi():
    def __init__(self,driver):
        # driver and wait variable creation
        self.driver = driver
        self.wait = WebDriverWait(driver,40)
        # locator of elements
        self.login_locator      = (By.ID, 'login-btn')
        self.signup_locator     = (By.XPATH, '//a[contains(text(),"Sign up")]')
        self.courses_locator    = (By.XPATH, '//div[2]/div/div[4]/a')
        self.liveclasses_locator= (By.XPATH, '//p[@id="liveclasseslink"]')
        self.practice_locator   = (By.XPATH, '//p[@id="practiceslink"]')
        self.dobbyguvi_locator  = (By.XPATH, '//*[@id="chateleon-container-gif-0"]')

    # checking Login display
    def login_isdisplayed(self):
        try:
            self.wait.until(ec.visibility_of_element_located(self.login_locator))
            login_displayed = self.driver.find_element(*self.login_locator).is_displayed()
            return True
        except Exception as e:
            return None

    # checking Login is clickable
    def login_isclickable(self):
        try:
            login_clickable = self.driver.find_element(*self.login_locator).click()
            return True
        except Exception as e:
            print(f"Exception: e")
            return None

    # To perform click login
    def click_login(self):
        self.driver.find_element(*self.login_locator).click()

    # checking Signup display
    def signup_isdisplayed(self):
        try:
            self.wait.until(ec.visibility_of_element_located(self.signup_locator))
            signup_displayed = self.driver.find_element(*self.signup_locator).is_displayed()
            return True
        except Exception as e:
            print(f"Exception: {e}")
            return None

    # checking Signup is clickable
    def signup_isclickable(self):
        try:
            signup_clickable = self.driver.find_element(*self.signup_locator).click()
            return True
        except Exception as e:
            print(f"Exception: {e}")
            return None

    # checking menu items Courses, Liveclasses, Practices display and accessibility
    def menu_items_display_enable(self):
        try:
            self.wait.until(ec.visibility_of_element_located(self.courses_locator))
            self.driver.find_element(*self.courses_locator).is_enabled()
            self.wait.until(ec.visibility_of_element_located(self.practice_locator))
            self.driver.find_element(*self.practice_locator).is_enabled()
            self.wait.until(ec.visibility_of_element_located(self.liveclasses_locator))
            self.driver.find_element(*self.liveclasses_locator).is_enabled()
            return True
        except Exception as e:
            print(f"Exception: {e}")

    # checking dobby assistant display
    def dobby_assistant_isdisplayed(self):
        try:
            self.wait.until(ec.visibility_of_element_located(self.dobbyguvi_locator))
            self.driver.find_element(*self.dobbyguvi_locator).is_displayed()
            return True
        except Exception as e:
            print(f"Exception: {e}")

    # To click Signup
    def click_signin(self):
        self.driver.find_element(*self.signup_locator).click()




