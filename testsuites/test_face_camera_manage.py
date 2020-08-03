#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import unittest
import os
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.face_face_camera_page import FACE
from ddt import ddt,data,unpack

class face(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        consolelogin = HomePage(self.driver)
        consolelogin.console_login_succ()
        time.sleep(1)
        consolelogin.open_face_camera()

    def tearDown(self):
        self.driver.quit()

    def test_01_add_camera2(self):
        elemts = (["", "", "", "", ""],
          ["", "80000", "admin", "123456yanfa", "188"],
          ["192.1和8.1.12", "80000", "admin", "123456yanfa", "188"],
          ["192.18.1g.12", "80000", "admin", "123456yanfa", "188"],
          ["19^.18.1.12", "80000", "admin", "123456yanfa", "188"],
          ["192.1.12", "80000", "admin", "123456yanfa", "188"],
          ["192.258.1.12", "80000", "admin", "123456yanfa", "188"],
          ["192.168.1.12", "0", "admin", "123456yanfa", "188"],
          ["192.168.1.12", "", "admin", "123456yanfa", "188"],
          ["192.168.1.12", "800050", "admin", "123456yanfa", "188"],
          ["192.168.1.12", "0及", "admin", "123456yanfa", "188"],
          ["192.168.1.12", "0jh", "admin", "123456yanfa", "188"],
          ["192.168.1.12", "0$", "admin", "123456yanfa", "188"],
          ["192.168.1.12", "80000", "", "123456yanfa", "188"],
          ["192.168.1.12", "80000", "admjr", "123456yanfa", "188"],
          ["192.168.1.12", "80000", "admin", "", "188"],
          ["192.168.1.12", "80000", "admin", "123%6yanfa", "188"],
          ["192.228.1.12", "80000", "admin", "kahf64", "188"],
          ["192.168.1.12", "80000", "admin", "123456yanfa", ""],
          ["192.168.1.12", "80000", "admin", "123456yanfa", "1884567"],
          ["192.168.1.12", "80000", "admin", "123456yanfa", "8"],
          ["192.168.1.12", "80000", "admin", "123456yanfa", "188456"],
          ["192.168.1.12", "80000", "admin", "123456yanfa", "188h"],
          ["192.168.1.12", "80000", "admin", "123456yanfa", "18计8"],
          ["192.168.1.12", "80000", "admin", "123456yanfa", "188("],
          ["192.168.1.12", "80000", "admin", "123456yanfa", "1188"],
          ["192.168.1.12", "80000", "admin", "123456yanfa", "1188"],
          ["192.168.1.12", "80000", "admin", "123456yanfa", "188"]
          )
        face = FACE(self.driver)
        time.sleep(2)
        face.add_camera2('')
        for val in elemts:
            try:
                face.input_add_message(val[0],val[1],val[2],val[3],val[4])
                time.sleep(1)
                face.click_confirm()
                time.sleep(1)
            except Exception as e:
                print("fail", format(e))

if __name__ == "__main__":
    unittest.main()

