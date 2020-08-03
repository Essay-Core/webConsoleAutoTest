#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.dive_time_page import Set_time

class Dive_time(unittest.TestCase):

    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        consolelogin = HomePage(self.driver)
        consolelogin.console_login_succ()
        time.sleep(1)
        consolelogin.open_divetime()

    def tearDown(self):
        self.driver.quit()

    def test_01_selectAweek(self):
        dive = Set_time(self.driver)
        dive.send_time()

if __name__ == "__main__":

    unittest.main()