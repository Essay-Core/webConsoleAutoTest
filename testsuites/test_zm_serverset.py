#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import  time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.zm_server_setpage import zmServerpage

class imsiSerSet(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        consolelogin = HomePage(self.driver)
        consolelogin.console_login_succ()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    def tt_zmser01_onlyMain_pass(self):
        elemts = (
            #["imisfiltime","serIp", "port"],
            ["8", "192.168.3.23", "1883"],
            ["60", "192.168.3.234", "1883"],
        )
        setSer = zmServerpage(self.driver)
        setSer.open_zmgl()
        time.sleep(1)
        setSer.open_zmServer()
        time.sleep(1)
        for val in elemts:
            setSer.clearFtime()
            setSer.type_imsiFilTime(val[0])
            setSer.clearMserIP()
            setSer.type_mainSerIP(val[1])
            setSer.clearMserPort()
            setSer.type_mainSerPort(val[2])
            if self.ifcheckBoxClicked() == True:
                setSer.setSec()
            time.sleep(1)
            setSer.saveSerPar()
            time.sleep(1)

    def test_zmser01_onlyMain_fail(self):
        elemts = (
            #["imisfiltime","serIp", "port"],
            ["中文", "192.168.3.23", "1883"],
            ["60", "192.168.3.234中文", "1883"],
            ["60", "192.168.3.234", "1883中文"],
            ["60", "192.168.3.234@", "1883中文"],
            ["60@", "192.168.3.234", "1883"],
            ["60", "192.168.3.234", "1883@"],
        )
        setSer = zmServerpage(self.driver)
        setSer.open_zmgl()
        time.sleep(1)
        setSer.open_zmServer()
        time.sleep(1)
        for val in elemts:
            setSer.clearFtime()
            setSer.type_imsiFilTime(val[0])
            setSer.clearMserIP()
            setSer.type_mainSerIP(val[1])
            setSer.clearMserPort()
            setSer.type_mainSerPort(val[2])
            if self.ifcheckBoxClicked() == True:
                setSer.setSec()
            time.sleep(1)
            setSer.saveSerPar()
            time.sleep(1)
            try:
                setSer.clicks_errconfirm()
                time.sleep(2)
            except Exception as err:
                print("info",format(err))


    def tt_zmser02_MainAndSec_pass(self):
        elemts = (
            # ["imisfiltime","serIp", "port"],
            ["60", "192.168.3.230", "1883", "192.168.3.234", "1883"],
            ["60", "192.168.3.230", "1883","192.168.3.234", "1883"],
        )
        setSer = zmServerpage(self.driver)
        setSer.open_zmgl()
        time.sleep(1)
        setSer.open_zmServer()
        time.sleep(1)

        for val in elemts:
            setSer.clearFtime()
            setSer.type_imsiFilTime(val[0])
            setSer.clearMserIP()
            setSer.type_mainSerIP(val[1])
            setSer.clearMserPort()
            setSer.type_mainSerPort(val[2])
            time.sleep(1)
            if self.ifcheckBoxClicked() == False:
                setSer.setSec()
            time.sleep(1)
            setSer.clearSecIP()
            setSer.type_secSerIP(val[3])
            setSer.clearSecport()
            setSer.type_secSerPort(val[4])
            time.sleep(1)
            setSer.saveSerPar()
            time.sleep(2)

    def ifcheckBoxClicked(self):
        check_on = '//span[@class="el-checkbox__input is-checked"]'
        try:
            self.driver.find_element_by_xpath(check_on)
            return True
        except Exception as err:
            print("fail", format(err))
            return False

if __name__ == '__main__':
    unittest.main()