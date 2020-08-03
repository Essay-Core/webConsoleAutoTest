#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import unittest
import time
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.ss_real_time_imsi_page import Rtime_imsi

class real_time_imsi(unittest.TestCase):
    def setUp(self):
        try:
            browse = BrowserEngine(self)
            self.driver = browse.open_browser(self)
            consolelogin = HomePage(self.driver)
            consolelogin.console_login_succ()
            time.sleep(1)
            consolelogin.open_real_time_imsi()
        except Exception as err:
            print(err)

    def tearDown(self):
        self.driver.quit()

    #下载
    def test_down_file(self):
        rtime_imsi = Rtime_imsi(self.driver)
        try:
            rtime_imsi.down_modefile()
        except Exception as err:
            print(err)

    #删除
    def test_delet_imsi(self):
        rtime_imsi = Rtime_imsi(self.driver)
        try:
            rtime_imsi.choice_all_imsi(self.driver)
            rtime_imsi.delete_imsi()
        except Exception as err:
            print(err)

    #新增失败
    def test_add_imsi_fail(self):
        rtime_imsi = Rtime_imsi(self.driver)
        elemts = ([""],
          ["46000787214700"],
          ["4600078721470094"],
          ["jhvbh对景挂画lsjdh"],
          ["4600078*@147009"],
          ["46000lje2147009"],
          )
        rtime_imsi.click_add_imsi()
        for text in elemts:
            try:
                rtime_imsi.input_imsi(text)
                time.sleep(1)
                rtime_imsi.click_err_confirm(self.driver)
            except Exception as err:
                print(err)

    #新增成功
    def test_add_imsi_pass(self):
        rtime_imsi = Rtime_imsi(self.driver)
        elemts = (
          ["111007872147468"],
          ["460007872147009"]
          )
        for val in elemts:
            try:
                rtime_imsi.add_imsi_input(val)
                time.sleep(1)
                rtime_imsi.refresh_list()
                time.sleep(1)
            except Exception as err:
                print(err)

    #导入目标用例



if __name__ == "__main__":
    unittest.main()