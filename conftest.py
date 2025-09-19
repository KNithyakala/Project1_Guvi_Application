import logging
import pytest
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Getting details from config file

config = configparser.ConfigParser()
config.read("config.ini")
browser = config.get("browser_settings","browser").lower()
url = config.get("browser_settings","url")
valid_username = config.get("login_details","valid_username")
valid_password = config.get("login_details","valid_password")
invalid_username = config.get("login_details","invalid_username")
invalid_password = config.get("login_details","invalid_password")


@pytest.fixture(scope="class") # set up and tear down
def driver():
    # driver set up
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService())
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService())
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser in config.ini:{browser}.\n"
                         f"Only chrome/firefox/edge/safari are allowed")
    driver.maximize_window()
    yield driver
    # tear down
    driver.quit()

# To get valid username and password
@pytest.fixture(scope="class")
def valid_credentials():
    return {"username":valid_username,"password":valid_password}

# To get invalid username and password
@pytest.fixture(scope="class")
def invalid_credentials():
    return {"username":invalid_username,"password":invalid_password}

# To get url
@pytest.fixture(scope="class")
def get_url():
    return url

# defining log file
def pytest_configure():
    logger = logging.getLogger() # Debug,Info,Warning,Error,Critical,Fatal
    logger.setLevel(logging.INFO) # from where we need report
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler("test_logs.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)