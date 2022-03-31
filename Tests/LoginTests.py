import unittest
from selenium.webdriver.common.by import By
from Locators.LoginLocators import LoginLocator
from Pages.LoginPage import LoginPage


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.login = LoginPage()
        self.driver = self.login.driver

    # def test1_valid_email_and_password(self):
    #     self.login.send_login_params("branmelke808@gmail.com", "123456")
    #     res = self.driver.find_element(By.XPATH, LoginLocator.error_me).text
    #     self.assertTrue(True, True)

    def test2_invalid_email_and_valid_password(self):
        self.login.send_login_params("fail@gmail.com", "123456")
        res = self.driver.find_element(By.XPATH, LoginLocator.error_1).text
        self.assertIn("אופס", res, "Test Fail")

    def test3_valid_email_and_invalid_password(self):
        self.login.send_login_params("branmelke808@gmail.com", "xxxx")
        res = self.driver.find_element(By.XPATH, LoginLocator.error_1).text
        self.assertIn("אופס", res, "Test Fail")

    def test4_invalid_email_and_invalid_password(self):
        self.login.send_login_params("fail@gmail.com", "xxxx")
        res = self.driver.find_element(By.XPATH, LoginLocator.error_1).text
        self.assertIn(" כתובת המייל אינה נכונה", res , "Login Page is stuck")

    def test5_email_land_password_are_left_blank(self):
        # self.login.send_login_params(" ", " ")
        self.driver.find_element(By.XPATH, LoginLocator.submit).click()
        em = self.driver.find_element(By.XPATH, LoginLocator.errno_em).text
        pa = self.driver.find_element(By.XPATH, LoginLocator.errno_pas).text
        self.assertEqual(em, pa, "Test Fail")

    def tearDown(self):
        self.driver.close()
