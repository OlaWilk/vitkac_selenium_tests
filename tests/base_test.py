import unittest
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import Firefox
from pages.home_page import HomePage

class BaseTest(unittest.TestCase):

    """
    Base class for each test.
    Using Firefox WebDriver manager.
    """

    def setUp(self):

        self.driver = Firefox(executable_path=GeckoDriverManager().install())
        self.driver.get("https://www.vitkac.com/pl")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.home_page = HomePage(self.driver)
        self.home_page.close_cookie_alert()

    def tearDown(self):
        self.driver.quit()