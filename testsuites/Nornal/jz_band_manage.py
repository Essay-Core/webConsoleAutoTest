#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import  time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.band_manage_page import BCBBandManage

class BCBband_mange(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        consolelogin = HomePage(self.driver)
        consolelogin.console_login_succ()
        time.sleep(1)
        consolelogin.open_band_manage()

    def tearDown(self):
        self.driver.quit()

    def test_01_set_par(self):
        bandPar = BCBBandManage(self.driver)
        bandPar.click_band_1()
        bandPar.click_setpar_band()
        bandPar.type_cellid("111")



if __name__ == "__main__":
    unittest.main()