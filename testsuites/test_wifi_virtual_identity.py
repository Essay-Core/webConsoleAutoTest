#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.wifi_server_page import WIFI_server

class virtual_identity(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        consolelogin = HomePage(self.driver)
        consolelogin.console_login_succ()
        time.sleep(1)
        consolelogin.open_virtual_data()

    def tearDown(self):
        self.driver.quit()

    reflash = '//button[@class="el-button reflashBtn el-button--primary is-plain"]'
    def test_01_onlymainserver(self):
        self.driver.find_element_by_xpath(self.reflash).click()
        time.sleep(3)



if __name__  == "__main__":
    unittest.main()