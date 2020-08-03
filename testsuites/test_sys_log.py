#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.sys_downlog_page import LOG


class log(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        consolelogin = HomePage(self.driver)
        consolelogin.console_login_succ()
        time.sleep(1)
        consolelogin.open_download_log()

    def tearDown(self):
        self.driver.quit()

    def test_01_load_all_console_log(self):#主控全部日志
        log = LOG(self.driver)
        log.load_console_log_all()
        log.get_windows_img()


if __name__ == "__main__":
    unittest.main()


