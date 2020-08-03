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

    def test_zmser01_onlyMain(self):
        setSer = zmServerpage(self.driver)
        setSer.open_zmgl()
        time.sleep(1)
        setSer.open_zmServer()
        time.sleep(1)
        setSer.clearFtime()
        setSer.type_imsiFilTime("60")
        setSer.clearMserIP()
        setSer.type_mainSerIP("192.168.3.234")
        setSer.clearMserPort()
        setSer.type_mainSerPort("1883")
        txt = self.driver.find_element_by_xpath("//*[@id='app']/section/section/main/div/div[2]/div[3]/div/div[2]/form/div[7]/div/label").get_attribute("class")
        if txt == "el-checkbox is-checked":
            setSer.setSec()
        time.sleep(1)
        setSer.saveSerPar()
        time.sleep(2)
        setSer.get_windows_img()  # 调用基类截图方法

    def test_zmser02_MainAndSec(self):
        setSer  = zmServerpage(self.driver)
        setSer.open_zmgl()
        time.sleep(1)
        setSer.open_zmServer()
        time.sleep(1)
        setSer.clearFtime()
        setSer.type_imsiFilTime("60")
        setSer.clearMserIP()
        setSer.type_mainSerIP("192.168.3.230")
        setSer.clearMserPort()
        setSer.type_mainSerPort("1883")
        time.sleep(1)
        txt = self.driver.find_element_by_xpath(
            "//*[@id='app']/section/section/main/div/div[2]/div[3]/div/div[2]/form/div[7]/div/label").get_attribute(
            "class")
        print(txt)
        if txt == "el-checkbox":
            print("1")
            setSer.setSec()
        time.sleep(1)
        setSer.clearSecIP()
        setSer.type_secSerIP("192.168.3.234")
        setSer.clearSecport()
        setSer.type_secSerPort("1883")
        time.sleep(1)
        setSer.saveSerPar()
        time.sleep(2)
        setSer.get_windows_img()  # 调用基类截图方法


if __name__ == '__main__':
    unittest.main()

