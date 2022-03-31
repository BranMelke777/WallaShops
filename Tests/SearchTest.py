import unittest
from selenium.webdriver.common.by import By
from Locators.SearchLocators import SearchLocators
from Pages.SearchPage import SearchPage


class SearchTest(unittest.TestCase):

    def setUp(self):
        self.search = SearchPage()
        self.driver = self.search.driver
        self.pro_name = "מחשב נייח מחודש Lenovo דגם M93 עם זיכרון 8GB ומעבד"

    def test1_searchProduct(self):
        res = self.search.send_searchProduct(self.pro_name)
        self.assertIn(True, res)

    def test2_clickProduct(self):
        res = self.search.send_searchProduct(self.pro_name)
        res[1].click()
        pro = self.driver.find_element(By.XPATH, SearchLocators.product_page).text
        self.assertIn(self.pro_name, pro, "Fail: Product Page Not Found")

    def test3_searchEmpty(self):
        self.driver.find_element(By.XPATH, SearchLocators.search).send_keys("")
        self.driver.find_element(By.XPATH, SearchLocators.search_button).click()
        res = self.driver.find_element(By.XPATH, SearchLocators.search_result).text
        self.assertIn("0 מתוך 0", res, "Fail: Result exist")
