#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.sys_downlog_page import LOG


class log_alarm(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        consolelogin = HomePage(self.driver)
        consolelogin.console_login_succ()
        time.sleep(1)
        consolelogin.open_alarm_log()

    def tearDown(self):
        self.driver.quit()

    inqury = '(//button[@class="el-button el-button--primary is-plain"])[1]'
    reflash = '(//button[@class="el-button el-button--primary is-plain"])[2]'

    def test_reflash(self):
        self.driver.find_element_by_xpath(self.inqury).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.reflash).click()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()


