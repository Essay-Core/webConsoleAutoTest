#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
from framework.base_page import BasePage

class route_track(BasePage):
    test_ip = "xpath=>//input[@placeholder='请输入IP']"
    ping = "xpath=>//span[text()='ping']"

    def ping_ip(self,ip):
        self.inputText(self.test_ip, ip)
        self.clicks(self.ping)
        time.sleep(10)