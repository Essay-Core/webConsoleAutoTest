#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from framework.base_page import BasePage
import time


class KB_Real_Time_Elemts(BasePage):
    #未使用
    reflash = '(//button[@class="el-button el-button--success el-button--medium"])[1]'
    clear = '(//button[@class="el-button el-button--success el-button--medium"])[2]'

    def click_reflash(self):
        self.clicks(self.reflash)
        time.sleep(1)

    def click_clear(self):
        self.clicks(self.clear)
        time.sleep(1)
