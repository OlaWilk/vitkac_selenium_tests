import unittest
from base_test import BaseTest
from pages.new_account_page import NewAccountPage
from tests.test_data import TestData
from pages.locators import NewAccountPageLocators
from pages.home_page import HomePage

class NewAccountTest(BaseTest):

    def test_invalid_email(self):

        # 1. Go to the registration page
        HomePage.click_sign_in(self)
        # 2. Enter First Name
        NewAccountPage.enter_name(self, TestData.first_name)
        # 3. Enter Last Name
        NewAccountPage.enter_last_name(self, TestData.last_name)
        # 4. Please enter an incorrect e-mail
        NewAccountPage.enter_invalid_email(self, TestData.invalid_email)
        # 5. Select a gender
        NewAccountPage.choose_gender(self, TestData.sex)
        # 6. Enter Password
        NewAccountPage.enter_password(self, TestData.password)
        # 7. Confirm Password
        NewAccountPage.enter_password_again(self, TestData.password)
        # 8. Accept the regulations
        NewAccountPage.click_checkboxes(self)
        # 9. Click "Register"
        NewAccountPage.click_register_btn(self)
        # EXPECTED RESULT - message about incorrect e-mail provided
        self.assertEqual(NewAccountPageLocators.ERROR_ALERT_EXPECTED, NewAccountPage.get_errors_alert(self))

if __name__ == "__main__":
    unittest.main()