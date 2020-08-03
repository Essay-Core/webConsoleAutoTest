#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage

class Filt_IMSI(BasePage):
    clear_list = "xpath=>//span[text()='清空']"

    def clear_imsi_list(self):
        self.clicks(self.clear_list)