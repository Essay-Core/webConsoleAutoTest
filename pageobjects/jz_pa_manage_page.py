#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import time
from framework.base_page import BasePage
class PA_manage(BasePage):
    # refresh = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[4]/div[1]/div/button[1]/span"#刷新按钮
    refresh = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[1]/div/button[1]/span"
    pa_on = "xpath=>//span[text()='开启所有功放']"

    pa_off = "xpath=>//span[text()='关闭所有功放']"

    def click_refresh_pa(self):
        self.clicks(self.refresh)
        time.sleep(2)

    def click_pa_on_all(self):
        self.clicks(self.pa_on)
        time.sleep(1)

    def click_pa_off_all(self):
        self.clicks(self.pa_off)
        time.sleep(1)