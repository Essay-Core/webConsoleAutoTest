#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.jz_alarm_set_page import Alarm_set

class alarm_set(unittest.TestCase):

    def setUp(self):
        browse = BrowserEngine(self)
        try:
            self.driver = browse.open_browser(self)
            consolelogin = HomePage(self.driver)
            consolelogin.console_login_succ()
            time.sleep(1)
            consolelogin.open_alarm_set()
        except Exception as err:
            print("fail",format(err))

    def tearDown(self):
        self.driver.quit()


    def test_setalarm_on_pass(self):
        setalarm = Alarm_set(self.driver)
        if self.ifcheckBoxClicked() == False:
            setalarm.chioce_ifon()
        items = (
            "-1",
            "1",
            "65535",
            "65536"
            "20"
        )
        for val in items:
            try:
                setalarm.set_alarm(val)
                setalarm.savepar()
                time.sleep(1)
                print("pass")
            except Exception as err:
                print("fail",format(err))

    def test_setalarm_on_fail(self):
        setalarm = Alarm_set(self.driver)
        if self.ifcheckBoxClicked() == False:
            setalarm.chioce_ifon()
        items = (
            "中文1",
            "中文2",
        )
        for val in items:
            try:
                setalarm.set_alarm(val)
                time.sleep(1)
                setalarm.savepar()
                time.sleep(1)
                setalarm.clicks_errconfirm()
                time.sleep(1)
                print("pass")
            except Exception as err:
                print("fail",format(err))


    def test_setalarm_off(self):
        setalarm = Alarm_set(self.driver)
        if self.ifcheckBoxClicked() == True:
            setalarm.chioce_ifon()
        setalarm.savepar()
        time.sleep(2)

    def ifcheckBoxClicked(self):
        check_on = '//span[@class="el-checkbox__input is-checked"]'
        try:
            self.driver.find_element_by_xpath(check_on)
            return True
        except Exception as err:
            print("fail", format(err))
            return False





if __name__ == "__main__":
    unittest.main()
