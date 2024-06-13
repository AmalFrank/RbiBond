import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utlities.readProperties import ReadConfig
from utlities.customLogger import LogGen

class Test_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homepage(self, setup):
        self.logger.info("*********** Test_Login **********")
        self.logger.info("*********** Verifying Home Page Title **********")
        self.driver=setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        time.sleep(10)
        act_title=self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*********** Home page title test is passed **********")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("*********** Home page title test is failed **********")
            assert False

    def test_login(self, setup):
        self.logger.info("*********** Verifying Login **********")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        time.sleep(5)
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.clickLogin()
        time.sleep(10)
        act_title = self.driver.title
        self.lp.clickLogout()
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("*********** Login test is passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.info("*********** Login test is failed **********")
            self.driver.close()
            assert False





