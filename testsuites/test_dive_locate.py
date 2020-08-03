#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.dive_locate_page import Set_locate

class Dive_locate(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        consolelogin = HomePage(self.driver)
        try:
            consolelogin.console_login_succ()
            time.sleep(1)
            consolelogin.open_divelocate()
        except Exception as err:
            print("fail", format(err))

    def tearDown(self):
        self.driver.quit()

    def test_setLocateMessage_pass(self):
        elemts = (
            ["25.2","25.2"],
            ["25.7", "33.2"],
        )
        dive = Set_locate(self.driver)
        for val in elemts:
            try:
                dive.set_message(val[0], val[1])
                dive.save()
                print("pass")
            except Exception as err:
                print("fail", format(err))

    def test_setLocateMessage_fail(self):
        elemts = (
            ["25.", "25.0"],
            ["-1","25.0"],
            ["中文", "25.0"],
            ["25@", "25.0"],
            ["25.0", "25."],
            ["25.0", "-1"],
            ["25.0", "中文"],
            ["25.0", "25@"],
            ["25.0", ""],
        )
        dive = Set_locate(self.driver)
        for val in elemts:
            try:
                dive.set_message(val[0], val[1])
                dive.save()
                dive.clicks_errconfirm()
                print("pass")
            except Exception as err:
                print("fail",format(err))


if __name__ == "__main__":
    unittest.main()