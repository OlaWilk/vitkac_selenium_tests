from pages.base_page import BasePage
from pages.locators import HomePageLocators, PurchasePageLocators


class PurchasePage(BasePage):

    def close_cookie_alert(self):
        el = self.driver.find_element(*HomePageLocators.COOKIE_ALERT)
        el.click()

    def woman_site(self):
        el = self.driver.find_element(*PurchasePageLocators.WOMEN_SITE)
        el.click()

    def product_site(self):
        el = self.driver.find_element(*PurchasePageLocators.EXAMPLE_PRODUCT)
        el.click()

    def add_product(self):
        el = self.driver.find_element(*PurchasePageLocators.ADD_PRODUCT)
        el.click()

    def refresh(self):
        self.driver.refresh()

    def purchase_info(self):
        shop_info = self.driver.find_element(*PurchasePageLocators.SHOP_INFO).text
        return shop_info

