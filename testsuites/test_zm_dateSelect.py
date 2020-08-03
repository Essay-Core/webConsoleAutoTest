#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import  time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.zm_datapage import zmDataPage

class imsiData(unittest.TestCase):

    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        consolelogin = HomePage(self.driver)
        consolelogin.console_login_succ()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    def test_01_selectAweek(self):
        imsid = zmDataPage(self.driver)
        imsid.open_zmgl()
        time.sleep(1)
        imsid.open_zmdata()
        time.sleep(1)
        imsid.chioce_startime()
        time.sleep(1)
        imsid.chioce_week()
        time.sleep(1)
        imsid.selectImsidate()
        time.sleep(2)
        imsid.exportData()
        time.sleep(1)
        imsid.outcomfirm()
        time.sleep(5)
        imsid.get_windows_img()

if __name__ == "__main__":
    unittest.main()