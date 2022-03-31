from selenium.webdriver.common.by import By
from selenium import webdriver
from Locators.SearchLocators import SearchLocators


class SearchPage(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.wallashops.co.il")
        # self.driver.maximize_window()

    def send_searchProduct(self, product):
        self.driver.find_element(By.XPATH, SearchLocators.search).send_keys(product)
        res = False
        el = self.driver.find_element(By.XPATH, SearchLocators.item_op)
        if el:
            res = True
        return res, el
