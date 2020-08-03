#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import unittest
import os
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.plate_plate_camera_page import Plate_camera
from ddt import ddt,data,unpack

class plate_camera(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        consolelogin = HomePage(self.driver)
        consolelogin.console_login_succ()
        time.sleep(1)
        consolelogin.open_palte_camera()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    def test_add_camera_pass(self):
        elemts = (
                  ["192.168.2.121", "8888", "admin", "123456", "654321"],
                  ["192.168.2.122", "9999", "admin", "123456yanfa", "123456"],
                  )
        face = Plate_camera(self.driver)
        time.sleep(2)

        for val in elemts:
            try:
                print("ip:%s port:%s user:%s passwd:%s camera id:%s" % (val[0], val[1], val[2], val[3], val[4]))
                face.click_add_camera()
                time.sleep(1)
                face.input_add_message(val[0], val[1], val[2], val[3], val[4])
                time.sleep(1)
                face.click_confirm()
                time.sleep(2)
                print("pass")
            except Exception as e:
                print("fail", format(e))
                return

    def test_add_camera_fail(self):
        elemts = (["1", "2", "3", "4", "5"],
          ["", "80000", "admin", "123456yanfa", "188"],
          ["192.1和8.1.12", "80000", "admin", "123456yanfa", "188"],
          ["192.18.1g.12", "80000", "admin", "123456yanfa", "188"],
          ["19^.18.1.12", "80000", "admin", "123456yanfa", "188"],
          ["192.258.1.12", "800000", "admin", "123456yanfa", "188"],
          ["192.168.1.12", "", "admin", "123456yanfa", "188"],
          ["192.168.1.12", "800050", "", "123456yanfa", "188"],
          ["192.168.1.12", "0及", "admin", "", "188"],
          ["192.168.1.12", "0jh", "admin", "123456yanfa", ""],
          ["192.168.1.12", "0$", "admin", "123456yanfa", "188"],
          ["192.168.1.12", "80000", "$", "123456yanfa", "188"],
          ["192.168.1.12", "80000", "admjr", "123$456yanfa", "188"],
          ["192.168.1.12", "80000", "admin", "", "18$8"],
          ["192.168.1.12", "8中文0", "admin", "123%6yanfa", "188"],
          ["192.228.1.12", "80000", "adm中文in", "kahf64", "188"],
          ["192.168.1.12", "80000", "admin", "12345中文6yanfa", ""],
          ["192.168.1.12", "80000", "admin", "123456yanfa", "188中文4567"],
          )
        face = Plate_camera(self.driver)
        face.click_add_camera()
        time.sleep(1)
        for val in elemts:
            try:
                print("ip:%s port:%s user:%s passwd:%s camera id:%s"%(val[0],val[1],val[2],val[3],val[4]))
                face.input_add_message(val[0],val[1],val[2],val[3],val[4])
                time.sleep(1)
                face.click_confirm()
                time.sleep(1)
                print("pass")
            except Exception as e:
                print("fail", format(e))
                return


if __name__ == "__main__":
    unittest.main()

