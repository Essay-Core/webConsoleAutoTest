#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import unittest
import time
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage

class random_access(unittest.TestCase):
    def setUp(self):
        try:
            browse = BrowserEngine(self)
            self.driver = browse.open_browser(self)
            consolelogin = HomePage(self.driver)
            consolelogin.console_login_succ()
            time.sleep(1)
            consolelogin.open_radom_access()
        except Exception as err:
            print(err)

    def tearDown(self):
        self.driver.quit()

    reflash = '(//button[@class="el-button el-button--success el-button--medium"])[1]'
    clear = '(//button[@class="el-button el-button--success el-button--medium"])[2]'
    rrc_reflash = '//input[@placeholder="请输入RRC查询间隔（秒）"]'

    def test_reflash(self):
        self.driver.find_element_by_xpath(self.rrc_reflash).clear()
        self.driver.find_element_by_xpath(self.rrc_reflash).send_keys("5")
        time.sleep(1)
        self.driver.find_element_by_xpath(self.clear).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.reflash).click()
        time.sleep(10)





if __name__ == "__main__":
    unittest.main()