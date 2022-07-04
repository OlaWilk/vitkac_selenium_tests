import unittest
from base_test import BaseTest
from pages.locators import PurchasePageLocators
from pages.purchase_page import PurchasePage

class PurchaseTest(BaseTest):

    def testPurchase(self):

        # 1. Go to the "Women" tab
        PurchasePage.woman_site(self)
        # 2. Go to the sample product page
        PurchasePage.product_site(self)
        # 3. Add the product to the cart
        PurchasePage.add_product(self)
        # 4. Refresh page
        PurchasePage.refresh(self)
        #EXPECTED RESULT- 1 product in the cart
        self.assertEqual(PurchasePageLocators.SHOP_INFO_EXPECTED, PurchasePage.purchase_info(self))

if __name__ == "__main__":
    unittest.main()