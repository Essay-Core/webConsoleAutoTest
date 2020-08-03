#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.wifi_server_page import WIFI_server

class wifi_server(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        consolelogin = HomePage(self.driver)
        consolelogin.console_login_succ()
        time.sleep(1)
        consolelogin.open_wifi_server_manage()

    def tearDown(self):
        self.driver.quit()

    def test_01_onlymainserver_pass(self):
        wifi_server = WIFI_server(self.driver)
        wifi_server.type_main_ip("192.168.3.230")
        wifi_server.type_main_port("1983")
        if self.ifcheckBoxClicked() == True:
            wifi_server.click_if_sec()
        wifi_server.click_save()

    def test_01_onlymainserver_fail(self):
        elemts = (
            #["mainip","mainPort","secondIP","secondPort"],
            ["192.168.3.230中文","1983","192.168.3.1","8888"],
            ["192.168.3.230", "1983中文", "192.168.3.1", "8888"]
        )
        wifi_server = WIFI_server(self.driver)
        for val in elemts:
            wifi_server.type_main_ip(val[0])
            wifi_server.type_main_port(val[1])
            if self.ifcheckBoxClicked() == False:
                wifi_server.click_if_sec()
            wifi_server.type_sec_ip(val[2])
            wifi_server.type_main_port(val[3])
            time.sleep(1)
            wifi_server.click_save()
            time.sleep(1)
            try:
                wifi_server.clicks_errconfirm()
                time.sleep(2)
            except Exception as err:
                print("info", format(err))

    def ifcheckBoxClicked(self):
        check_on = '//span[@class="el-checkbox__input is-checked"]'
        try:
            self.driver.find_element_by_xpath(check_on)
            return True #被选返回真
        except Exception as err:
            return False

if __name__  == "__main__":
    unittest.main()