import logging

from Project1_Guvi_Application.pages.dashboard_page import Dashboard_guvi
from Project1_Guvi_Application.pages.home_page import Homepage_guvi
from Project1_Guvi_Application.pages.login_page import Login_guvi
from Project1_Guvi_Application.pages.register_page import Register_guvi

class Test_Guvi_app():
    # Test Case 1 - Validating url
    def test_validate_url(self,driver,get_url):
        try:
            expected_url = get_url
            global homepage # making homepage instance as global so that it can be accessible from other method
            homepage = Homepage_guvi(driver)
            driver.get(expected_url)
            assert driver.current_url == expected_url
            logging.info("The application is loaded successully.")
            driver.save_screenshot("my_screenshots\Pass_testcases\TC01_Pass.png")

        except Exception as e:
            logging.info(f"Expected {expected_url}, but got {driver.current_url}")
            driver.save_screenshot("my_screenshots\Fail_testcases\TC01_Fail.png")

    # Test Case 2 - Validating title
    def test_validate_title(self,driver):

        try:
            expected_title = "GUVI | Learn to code in your native language"
            assert driver.title == expected_title
            logging.info(f"The title is displayed as {driver.title}.")
            driver.save_screenshot("my_screenshots\Pass_testcases\TC02_Pass.png")

        except Exception as e:
            logging.info(f"Expected Title:{expected_title}, but title of page is displayed as{driver.title}")
            driver.save_screenshot("my_screenshots\Fail_testcases\TC02_Fail.png")

    # Test Case 9 - Dobby Assistant display
    def test_validate_dobby_assistant(self,driver):

        try:
            assert homepage.dobby_assistant_isdisplayed()
            logging.info("Dobby Assistant is displayed on Home Page.")
            driver.save_screenshot("my_screenshots\Pass_testcases\TC09_Pass.png")

        except Exception as e:
            logging.info(f"Dobby Assistant is not displayed.")
            driver.save_screenshot("my_screenshots\Fail_testcases\TC09_Fail.png")

    # Test Case 8 - Menu Items Courses, Live Classes, Practices display
    def test_validate_menu_items(self,driver):

        try:
            assert homepage.menu_items_display_enable()
            logging.info("Courses, Live Classes and Practices are displayed and accessible on Home Page.")
            driver.save_screenshot("my_screenshots\Pass_testcases\TC08_Pass.png")

        except Exception as e:
            logging.info(f"Menu Items are not displayed and enabled.")
            driver.save_screenshot("my_screenshots\Fail_testcases\TC08_Fail.png")

    # Test Case 4 - Signup - Register Page
    def test_validate_signup(self,driver):
        try:
            assert homepage.signup_isdisplayed() and homepage.signup_isclickable()
            logging.info("Signup is displayed and enabled on Home Page.")
            assert "https://www.guvi.in/register/" == driver.current_url
            logging.info("Register Page is displayed when clicking Sign up button on Home Page.")
            driver.save_screenshot("my_screenshots\Pass_testcases\TC04_Pass.png")
            driver.back()
        except Exception as e:
            logging.info(f"It is not navigated to Register Page.")
            driver.save_screenshot("my_screenshots\Fail_testcases\TC04_Fail.png")

    # Test Case 5 - Sign-In page via Signup button
    def test_validate_signin_page_signup_button(self,driver,valid_credentials):
        try:
            homepage.click_signup()
            global register_page # making register_page instance as global so that it can be accessible from other method
            register_page = Register_guvi(driver)
            register_page.enter_details()
            driver.back()
            homepage.click_signup()
            signup = Register_guvi(driver)
            signup.click_login_link()
            assert "https://www.guvi.in/sign-in/"==driver.current_url
            logging.info("Sign-In Page is displayed when click Login on Register Page.")
            global login # making login instance as global so that it can be accessible from other method
            login = Login_guvi(driver)
            login.enter_email(valid_credentials["username"])
            login.enter_password(valid_credentials["password"])
            login.click_login_button()
            global dashboard # making dashboard instance as global so that it can be accessible from other method
            dashboard = Dashboard_guvi(driver)
            dashboard.welcome_message()
            assert "https://www.guvi.in/student-dashboard/" == driver.current_url
            logging.info("We are able to Login after registering the details.")
            driver.save_screenshot("my_screenshots\Pass_testcases\TC05_Pass.png")
            dashboard.logout()
        except Exception as e:
            logging.info(f"It is redirected to Register Page.{driver.current_url}")
            driver.save_screenshot("my_screenshots\Fail_testcases\TC05_Fail.png")

    # Test Case 3 - Validating Login button in Homepage
    def test_validate_login_button(self,driver):
        try:
            assert homepage.login_isdisplayed() and homepage.login_isclickable()
            logging.info("Login button is displayed and enabled.")
            assert "https://www.guvi.in/sign-in/"==driver.current_url
            logging.info("User is able to navigate to Sign-In page when clicking Login button on Home Page.")
            driver.save_screenshot("my_screenshots\Pass_testcases\TC03_Pass.png")
        except Exception as e:
            logging.info(f"It is not navigated to Signin page.")
            driver.save_screenshot("my_screenshots\Fail_testcases\TC03_Fail.png")

    # Test Case 7 - Validating Login with invalid credentials
    def test_validate_login_invalid_credentials(self, driver,invalid_credentials):
        try:
            homepage.click_login()
            login.enter_email(invalid_credentials["username"])
            login.enter_password(invalid_credentials["password"])
            login.click_login_button()
            error = login.get_error_message()
            assert "Incorrect" in error
            logging.info("Error message is displayed for invalid username and password.")
            driver.save_screenshot("my_screenshots\Pass_testcases\TC07_Pass.png")
        except Exception as e:
            logging.info(f"Error message is not displayed.")
            driver.save_screenshot("my_screenshots\Fail_testcases\TC07_Fail.png")

    # Test Case 6 - Validating Login with valid credentials
    def test_validate_login_valid_credentials(self,driver,valid_credentials):
        try:
            homepage.click_login()
            login.enter_email(valid_credentials["username"])
            login.enter_password(valid_credentials["password"])
            login.click_login_button()
            dashboard.welcome_message()
            assert "https://www.guvi.in/student-dashboard/" == driver.current_url
            logging.info("User is able to navigate to dashboard page with valid credentials.")
            driver.save_screenshot("my_screenshots\Pass_testcases\TC06_Pass.png")
        except Exception as e:
            logging.info(f"It is not redirected the Dashboard page.")
            driver.save_screenshot("my_screenshots\Fail_testcases\TC06_Fail.png")

    # Test Case 10 - Validating Logout functionality
    def test_validate_logout_functionality(self,driver,get_url):
        try:
            dashboard.logout()
            homepage.dobby_assistant_isdisplayed()
            assert get_url == driver.current_url
            logging.info("Logout is done properly.")
            driver.save_screenshot("my_screenshots\Pass_testcases\TC10_Pass.png")
        except Exception as e:
            logging.info(f"Logout is not done properly.")
            driver.save_screenshot("my_screenshots\Fail_testcases\TC10_Fail.png")