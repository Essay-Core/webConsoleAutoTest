#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import unittest
import time
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.ss_filt_imsi_list_page import Filt_IMSI

class real_time_imsi(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        consolelogin = HomePage(self.driver)
        consolelogin.console_login_succ()
        time.sleep(1)
        consolelogin.open_filt_imsi_list()

    def tearDown(self):
        self.driver.quit()

    def test_01_clear_imsi(self):
        filt_imsi = Filt_IMSI(self.driver)
        filt_imsi.clear_imsi_list()
        filt_imsi.get_windows_img()

if __name__ == "__main__":
    unittest.main()