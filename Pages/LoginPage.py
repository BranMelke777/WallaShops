from selenium.webdriver.common.by import By
from selenium import webdriver
from Locators.LoginLocators import LoginLocator


class LoginPage(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.wallashops.co.il/login")
        # self.driver.maximize_window()

    def send_login_params(self, email, password):
        self.driver.find_element(By.XPATH, LoginLocator.email).send_keys(email)
        self.driver.find_element(By.XPATH, LoginLocator.password).send_keys(password)
        self.driver.find_element(By.XPATH, LoginLocator.submit).click()

