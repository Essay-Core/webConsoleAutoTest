#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.sys_passwd_manage_page import PASSWD

def getData():
    '''数据分离出来放到列表中'''
    return (
        ["123456","","123456"],
        ["1234#6","123456","123456"],
        ["123456","1发56","1发56"],
        ["123456", "#*456", "#*456"],
        ["123456", "123456", "123456"],
        ["123456", "12kjv^@#kjh3j&456", "12kjv^@#kjh3j&456"],
        ["133456", "123 好456", "123 好456"],
        ["123456", "123 好456", "123 好456"],
        ["123和*6", "113456", "113456"],
        ["123456", "13456", "333456"],
        ["123456", "123456", "123456"],
    )

class passwd(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        consolelogin = HomePage(self.driver)
        try:
            consolelogin.console_login_succ()
            time.sleep(1)
            consolelogin.open_passwd_manage()
        except Exception as err:
            print(err)

    def tearDown(self):
        self.driver.quit()


    def test_01_update_passwd(self):
        elemts = getData()
        passwd = PASSWD(self.driver)
        time.sleep(1)
        for val in elemts:
            try:
                print("old:%s,new1:%s,new2:%s"%(val[0], val[1], val[2]))
                passwd.update_passwd(val[0], val[1], val[2])
                passwd.click_err_confirm(self.driver)
                time.sleep(2)
            except Exception as err:
                print(err)


if __name__ == "__main__":
    unittest.main()


