#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import unittest
import os
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.wifi_mac_page import MAC

class mac(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        consolelogin = HomePage(self.driver)
        consolelogin.console_login_succ()
        time.sleep(1)
        consolelogin.open_mac_data()

    def tearDown(self):
        self.driver.quit()

    def test_01_select_week(self):
        mac = MAC(self.driver)
        mac.clear_select_time()
        time.sleep(1)
        mac.select_time_week()
        mac.click_select()
        time.sleep(2)



if __name__  == "__main__":
    unittest.main()