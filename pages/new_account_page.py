from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from tests.test_data import TestData
from pages.locators import NewAccountPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class NewAccountPage(BasePage):

    def enter_name(self, first_name):

        el = self.driver.find_element(*NewAccountPageLocators.FIRST_NAME)
        el.send_keys(first_name)

    def enter_last_name(self, last_name):

        el = self.driver.find_element(*NewAccountPageLocators.LAST_NAME)
        el.send_keys(last_name)

    def enter_password(self, password):
        el = self.driver.find_element(*NewAccountPageLocators.PASSWORD)
        el.send_keys(password)

    def enter_password_again(self, password):

        el = self.driver.find_element(*NewAccountPageLocators.REPEAT_PASSWORD)
        el.send_keys(password)

    def choose_gender(self, gender):
        """
        Select Male if gender is male and Female otherwise
        """
        sex_field = Select(self.driver.find_element(By.ID, "sf_guard_user_sex_id"))
        if TestData.sex == "female":
            sex_field.select_by_value("2")
        else:
            sex_field.select_by_value("1")

    def enter_invalid_email(self, email):

        el = self.driver.find_element(*NewAccountPageLocators.EMAIL)
        el.send_keys(email)

    def click_checkboxes(self):

        r1 = self.driver.find_element(*NewAccountPageLocators.FIRST_CHECKBOX)
        r1.click()

        r2 = self.driver.find_element(*NewAccountPageLocators.SECOND_CHECKBOX)
        r2.click()

    def click_register_btn(self):

        el = self.driver.find_element(*NewAccountPageLocators.SUBMIT)
        el.click()

    def get_errors_alert(self):

        error_alert = self.driver.find_element(*NewAccountPageLocators.ERROR_ALERT_POSITION).text
        return error_alert

