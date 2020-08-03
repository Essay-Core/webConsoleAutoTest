#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage
from pageobjects.sys_route_track import route_track


class log(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        consolelogin = HomePage(self.driver)
        consolelogin.console_login_succ()
        time.sleep(1)
        consolelogin.open_route_track()

    def tearDown(self):
        self.driver.quit()

    def test_01_route_track(self):
        route = route_track(self.driver)
        route.ping_ip("192.168.43.55")
        route.get_windows_img()

if __name__ == "__main__":
    unittest.main()


