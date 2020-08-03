#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.base_plmn_page_v1 import Set_plmn

class Dive_plmn(unittest.TestCase):

    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        consolelogin = HomePage(self.driver)
        consolelogin.console_login_succ()
        time.sleep(1)
        consolelogin.open_plmn()

    def tearDown(self):
        self.driver.quit()

    confirm = '//button[@class="el-button el-button--default el-button--small el-button--primary "]'
    def tt_06_delete_mcc(self):
        del_bt_1 = '(//button[@class="el-button el-button--danger el-button--mini is-plain is-circle"])[2]'

        for v in range(3):
            self.driver.find_element_by_xpath(del_bt_1).click()
            time.sleep(1)
            self.driver.find_element_by_xpath(self.confirm).click()
            time.sleep(1)

    #mcc
    def tt_05_plmn_add_mcc_pass(self):
        items = (
            ["111","111"],
            ["222", "222"],
            ["333", "333"]
        )
        plmn = Set_plmn(self.driver)
        for val in items:
            try:
                print("mcc:%s national code:%s" % (val[0], val[1]))
                plmn.click_add_mcc()
                plmn.input_mcc(val[0],val[1])
                print("pass")
            except Exception as err:
                print("fail", format(err))

    def tt_04_plmn_add_mcc_fail(self):
        items = (
            ["", "111"],
            ["a", "111"],
            ["-1", "111"],
            ["33@3", "111"],
            ["中文", "111"],
            ["111", ""],
            ["111", "a"],
            ["111", "-1"],
            ["111", "33@3"],
            ["111", "中文"],
            ["111", ""],
        )
        plmn = Set_plmn(self.driver)
        plmn.click_add_mcc()

        for val in items:
            try:
                print("mcc:%s national code:%s" % (val[0], val[1]))
                plmn.input_mcc(val[0], val[1])
                plmn.click_err_confirm()
                print("pass")
            except Exception as err:
                print("fail", format(err))


    def tt_03_del_mnc(self):
        last = '(//button[@class="el-button el-button--danger el-button--mini is-plain is-circle"])[last()]'

        try:
            self.driver.find_element_by_xpath(last).click()
            time.sleep(1)
            self.driver.find_element_by_xpath(self.confirm).click()
            time.sleep(1)
            print("pass")
        except Exception as err:
            print("fail",format(err))

    #mnc
    def tt_02_plmn_add_mnc_pass(self):
        items = (
            ["01", "11"],
            ["11", "21"],
        )
        plmn = Set_plmn(self.driver)
        for val in items:
            try:
                print("mnc:%s carrier:%s" % (val[0], val[1]))
                plmn.click_add_mnc()
                plmn.click_standard()
                plmn.input_mnc(val[0],val[1])
                print("pass")
            except Exception as err:
                print("fail", format(err))

    def test_01_plmn_add_mnc_fail(self):
        items = (
            ["", "111"],
            ["a", "111"],
            ["-1", "111"],
            ["33@3", "111"],
            ["中文", "111"],
            ["111", ""],
            ["111", "a"],
            ["111", "-1"],
            ["111", "33@3"],
            ["111", "中文"],
            ["111", ""],
        )
        plmn = Set_plmn(self.driver)
        plmn.click_add_mnc()
        plmn.click_standard()
        for val in items:
            try:
                print("mnc:%s carrier:%s" % (val[0], val[1]))
                plmn.input_mnc(val[0], val[1])
                plmn.click_err_confirm()
                print("pass")
            except Exception as err:
                print("fail", format(err))

    #删除
    #修改

if __name__ == "__main__":

    unittest.main()