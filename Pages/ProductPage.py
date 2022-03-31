from selenium.webdriver.common.by import By
from selenium import webdriver
from Locators.SearchLocators import SearchLocators


class ProductPage(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.wallashops.co.il/lenovo-thinkcentre-m93p-t-lenovo-thinkcentre-m93p-t"
                        "/7MXLenovoThinkcentreM93pTiny-S_4d85380b.html")
        # self.driver.maximize_window()
