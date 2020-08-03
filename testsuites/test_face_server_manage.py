#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.face_server_page import FACE_server

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
        consolelogin.open_face_server()

    def tearDown(self):
        self.driver.quit()

    def test_set_pat(self):
        face = FACE_server(self.driver)
        time.sleep(1)
        elemts = getData()
        for val in elemts:
            face.set_par(val[0], val[1], val[2])
            main_xpath = 'body > div.el-message-box__wrapper'
            main = self.driver.find_element_by_css_selector(main_xpath)
            main.find_element_by_css_selector('div.el-message-box__wrapper > div > div.el-message-box__btns > button').click()
            time.sleep(1)

if __name__ == "__main__":
    unittest.main()
