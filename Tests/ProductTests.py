import time
import unittest
from selenium.webdriver.common.by import By
from Locators.ProductLocators import ProductLocators
from Pages.ProductPage import ProductPage


class ProductTest(unittest.TestCase):

    def setUp(self):
        self.product = ProductPage()
        self.driver = self.product.driver

    def test1_clickBiggerSmallMemory(self):
        price = self.driver.find_element(By.XPATH, ProductLocators.price_txt).text
        self.driver.find_element(By.XPATH, ProductLocators.big_size).click()
        time.sleep(1)
        big_price = self.driver.find_element(By.XPATH, ProductLocators.price_txt).text
        small_price = None
        if price != big_price:
            self.driver.find_element(By.XPATH, ProductLocators.small_size).click()
            time.sleep(1)
            small_price = self.driver.find_element(By.XPATH, ProductLocators.price_txt).text
        self.assertEqual(small_price, price, "Fail: Price didn't changed")

    def test2_clickSelfCollection(self):
        self.driver.find_element(By.XPATH, ProductLocators.collection_button).click()
        time.sleep(2)
        res = self.driver.find_element(By.XPATH, ProductLocators.collection_ver).text
        self.assertIn("כתובת איסוף:", res, "Fail: self-collection details not displayed")

    def test3_addToCart(self):
        self.driver.find_element(By.XPATH, ProductLocators.add_cart).click()
        if self.driver.find_element(By.XPATH, ProductLocators.alert):
            self.driver.find_element(By.XPATH, ProductLocators.alert).click()
            time.sleep(2)
        res = self.driver.find_element(By.XPATH, ProductLocators.cart_added).text
        self.assertEqual(res, "הוספנו בהצלחה את המוצר לסל הקניות שלך", "Fail: product didn't added to the cart")
