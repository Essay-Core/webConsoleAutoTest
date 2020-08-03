#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from framework.base_page import BasePage
import time

class LOG(BasePage):
    console_log_all = "xpath=>//span[text()='主控全部日志(较大)']"
    console_all_confirm = 'xpath=>/html/body/div[3]/div/div[3]/button[2]/span'
    console_all_cancel = 'xpath=>/html/body/div[4]/div/div[3]/button[1]/span'
    console_log = "xpath=>//span[text()='主控当前日志']"
    console_log_confirm = 'xpath=>/html/body/div[4]/div/div[3]/button[2]/span'
    console_log_cancel = 'xpath=>/html/body/div[4]/div/div[3]/button[1]'
    wifi_log = "xpath=>//span[text()='wifi程序日志']"

    def load_console_log_all(self):
        self.clicks(self.console_log_all)
        time.sleep(1)
        self.clicks(self.console_all_confirm)
        time.sleep(10)