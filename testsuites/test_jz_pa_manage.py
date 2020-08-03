#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import  time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.jz_pa_manage_page import PA_manage

class pa_mange(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        consolelogin = HomePage(self.driver)
        consolelogin.console_login_succ()
        time.sleep(1)
        consolelogin.open_pa_manage()

    def tearDown(self):
        self.driver.quit()
    #
    def test_01_refresh_palist(self):
        pamange = PA_manage(self.driver)
        try:
            pamange.click_refresh_pa()
            print("pass")
        except Exception as err:
            print("fail",format(err))

    def test_02_pa_on_all(self):
        pamange = PA_manage(self.driver)
        try:
            pamange.click_pa_on_all()
            print("pass")
        except Exception as err:
            print("fail",format(err))


    def test_03_pa_off_all(self):
        pamange = PA_manage(self.driver)
        try:
            pamange.click_pa_off_all()
            print("pass")
        except Exception as err:
            print("fail",format(err))


if __name__ == "__main__":
    unittest.main()
