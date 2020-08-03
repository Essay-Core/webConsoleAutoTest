#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.band_manage_page import BCBBandManage

class BCBband_mange(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        consolelogin = HomePage(self.driver)
        consolelogin.console_login_succ()
        time.sleep(1)
        consolelogin.open_band_manage()

    def tearDown(self):
        self.driver.quit()

    def tet_set_FDDpar_pass(self):
        bandPar = BCBBandManage(self.driver)
        bandPar.click_band_1()

        elemts = (
            #["cellid0","arfcn1","pci2","tac3","capture_time4","scan_list5","rxgain6","UePMax7"],
            ["111", "100", "499", "2333", "5", "450,100,1825,1650,750,500", "22", "1"],
            ["111", "100", "499", "2333", "5", "450,100,1825,1650,750,500", "22", "1"],
        )
        for val in elemts:
            try:
                bandPar.click_setpar_band()
                bandPar.type_cellid(val[0])
                # bandPar.set_plnm("中国","[01] 联通")
                bandPar.choice_bandwidth_20()
                bandPar.type_arfcn(val[1])
                bandPar.type_pci(val[2])
                bandPar.type_tac(val[3])
                bandPar.choice_workmode_1()
                bandPar.type_capture_time(val[4])
                bandPar.choice_scan_all()
                bandPar.type_scan_list(val[5])
                bandPar.type_rxgain(val[6])
                bandPar.type_UePMax(val[7])
                bandPar.choice_reject_cause_13()
                bandPar.choice_activate_cell_on()
                bandPar.choice_imei_catch_on()
                bandPar.choice_UlPowerAlpha_80()
                time.sleep(1)
                bandPar.click_save_par()
                time.sleep(2)
                bandPar.click_box_confirm()
                time.sleep(3)
                print("pass")
            except Exception as err:
                print("err",format(err))

    def test_set_FDDpar_fail(self):
        bandPar = BCBBandManage(self.driver)
        bandPar.click_band_1()
        bandPar.click_setpar_band()
        elemts = (
            #["cellid0","arfcn1","pci2","tac3","capture_time4","scan_list5","rxgain6","UePMax7"],
            ["111", "100", "499", "2333", "5", "450,100,1825,1650,750,500中文", "22", "1"],
            ["111", "100", "499", "2333", "5", "450,100,1825,1650,750,500", "22", "1"],
        )
        for val in elemts:
            try:
                bandPar.type_cellid(val[0])
                # bandPar.set_plnm("中国","[01] 联通")
                bandPar.choice_bandwidth_20()
                bandPar.type_arfcn(val[1])
                bandPar.type_pci(val[2])
                bandPar.type_tac(val[3])
                bandPar.choice_workmode_1()
                bandPar.type_capture_time(val[4])
                bandPar.choice_scan_all()
                bandPar.type_scan_list(val[5])
                bandPar.type_rxgain(val[6])
                bandPar.type_UePMax(val[7])
                bandPar.choice_reject_cause_13()
                bandPar.choice_activate_cell_on()
                bandPar.choice_imei_catch_on()
                bandPar.choice_UlPowerAlpha_80()
                time.sleep(1)
                bandPar.click_save_par()
                time.sleep(2)
                bandPar.click_box_confirm()
                time.sleep(2)
                print("pass")
            except Exception as err:
                print("fail",format(err))

    def test_03_sacn_band(self):
        bandPar = BCBBandManage(self.driver)
        try:
            bandPar.click_band_1()
            bandPar.click_rescan()
            time.sleep(1)
        except Exception as err:
            print("fail", format(err))

    def test_04_export_bandlog(self):
        try:
            bandPar = BCBBandManage(self.driver)
            bandPar.click_band_1()
            bandPar.click_export_band_log()
            print("pass")
        except Exception as err:
            print("fail", format(err))

    def test_05_reboot_band(self):
        bandPar = BCBBandManage(self.driver)
        bandPar.click_band_1()
        bandPar.click_reboot_band()
        print("软重启")

    def test_06_reboot_shutdown_band(self):
        bandPar = BCBBandManage(self.driver)
        bandPar.click_band_1()
        bandPar.click_reboot_shutdown_band()
        print("断电重启")
        time.sleep(3)
        t= self.driver.find_element_by_xpath("//span[text()='离线']").text
        try:
            assert '离线' in t
            print("3s后状态：离线")
        except Exception as e:
            print("fail", format(e))
        time.sleep(20)
        t = self.driver.find_element_by_xpath("//span[text()='离线']").text
        try:
            assert '离线' in t
            print("20s后状态：离线")
        except Exception as e:
            print("fail", format(e))
        time.sleep(60)
        t = self.driver.find_element_by_xpath("//span[text()='在线']").text
        try:
            assert '在线' in t
            print("60s后状态：在线")
        except Exception as e:
            print("fail", format(e))

if __name__ == "__main__":
    unittest.main()