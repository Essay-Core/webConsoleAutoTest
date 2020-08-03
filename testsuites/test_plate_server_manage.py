#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.plate_server_page import Plate_server

def getData():
    '''数据分离出来放到列表中'''
    return (
            ["", "192.168.3.230", "27020"],
            ["1885534", "192.168.3.230", "27020"],
            ["5", "192.168.3.230", "27020"],
            ["188553", "192.168.3.230", "27020"],
            ["18h553", "192.168.3.230", "27020"],
            ["188加3", "192.168.3.230", "27020"],
            ["185&3", "192.168.3.230", "27020"],
            ["1885","","27020"],
            ["1885","192.168.就.230","27020"],
            ["1885","192.168.3.h30","27020"],
            ["1885","1*2.168.3.230","27020"],
            ["1885","192.168.3","27020"],
            ["1885","192.168.3.230","27020"],
            ["1885","192.168.3.230",""],
            ["1885","192.168.3.230","0"],
            ["1885","192.168.3.230","65535"],
            ["1885","192.168.3.230","65536"],
            ["1885","192.168.3.230","9"],
            ["1885","192.168.3.230","65和"],
            ["1885","192.168.3.230","270*"],
            ["1885", "192.168.3.230", "27020"]
        )

class face(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        consolelogin = HomePage(self.driver)
        consolelogin.console_login_succ()
        time.sleep(1)
        consolelogin.open_palte_server()

    def tearDown(self):
        self.driver.quit()

    def test_set_plate_pass(self):
        plate = Plate_server(self.driver)
        time.sleep(1)
        elemts = (
            ["188553", "192.168.3.230", "27020"],
            ["d", "192.168.3.230", "27020"],
            ["adf", "192.168.3.230", "27020"],
            ["你好达到", "192.168.3.230", "27020"],
            ["18h553", "192.168. 230", "270#20"],
            ["18h553", "192.168.3.230", "270 20"],
        )
        for val in elemts:
            print("id:%s ip:%s port:%s"%(val[0],val[1], val[2]))
            plate.input_server_messgae(val[0],val[1], val[2])
            plate.click_confirm()
            time.sleep(1)

if __name__ == "__main__":
    unittest.main()
