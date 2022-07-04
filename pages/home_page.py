from pages.base_page import BasePage
from pages.locators import HomePageLocators

class HomePage(BasePage):

    def close_cookie_alert(self):
        el = self.driver.find_element(*HomePageLocators.COOKIE_ALERT)
        el.click()

    def click_sign_in(self):
        """
        Clicks Sign In
        """
        el = self.driver.find_element(*HomePageLocators.USER_BTN)
        el.click()

        el2 = self.driver.find_element(*HomePageLocators.REGISTER_BTN)
        el2.click()