#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.sys_user_manage_page import User
from ddt import ddt,data,unpack

def getData():
    return (
        ["cdd11据","cdd","123456","123456","备注备注备注"],
        ["", "cdd", "123456", "123456", "备注备注备注"],
        ["cdd11", "好v56", "123456", "123456", "备注备注备注"],
        ["cdd1将1", "cdddfuhbbsr54638158465", "&123456", "&123456", "%备注备注备注"],
    )

class user(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        consolelogin = HomePage(self.driver)
        consolelogin.console_login_succ()
        time.sleep(1)
        consolelogin.open_user_manage()

    def tearDown(self):
        self.driver.quit()

    def test_add_user_fail(self):
        elemts = getData()
        user = User(self.driver)
        user.click_add()
        for val in elemts:
            try:
                user.add(val[0], val[1], val[2], val[3], val[4])
                user.click_err_confirm(self.driver)
            except Exception as err:
                print(err)

if __name__ == "__main__":
    unittest.main()


