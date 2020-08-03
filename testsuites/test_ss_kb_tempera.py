#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import unittest
import time
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage

class kb_temperature(unittest.TestCase):
    def setUp(self):
        try:
            browse = BrowserEngine(self)
            self.driver = browse.open_browser(self)
            consolelogin = HomePage(self.driver)
            consolelogin.console_login_succ()
            time.sleep(1)
            consolelogin.open_kb_tempera()
        except Exception as err:
            print(err)

    def tearDown(self):
        self.driver.quit()

    reflash = '//button[@class="el-button resetBtn el-button--text"]'

    def test_reflash(self):
        self.driver.find_element_by_xpath(self.reflash).click()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()