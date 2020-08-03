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

    def test_set_time_pass(self):
        dive = Set_time(self.driver)
        try:
            dive.set_time()
            print("pass")
        except Exception as err:
            print("fail", format(err))

    def test_ntp_sync_pass(self):
        dive = Set_time(self.driver)
        try:
            dive.sync_save()
            print("pass")
        except Exception as err:
            print("fail", format(err))

if __name__ == "__main__":

    unittest.main()