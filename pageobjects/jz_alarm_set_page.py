#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from framework.base_page import BasePage
import time

class Alarm_set(BasePage):
    ifon = 'xpath=>//span[@class="el-checkbox__inner"]'
    save_alarmpar = 'xpath=>//button[@class="el-button resetBtn el-button--text"]'
    alarm_time = 'xpath=>(//input[@class="el-input__inner"])[1]'
    errConfirm = 'xpath=>//button[@class="el-button el-button--default el-button--small el-button--primary "]'
    def set_alarm(self,text):
        self.inputText(self.alarm_time, text)
        time.sleep(1)

    def chioce_ifon(self):
        self.clicks(self.ifon)

    def savepar(self):
        self.clicks(self.save_alarmpar)

    def clicks_errconfirm(self):
        self.clicks(self.errConfirm)
        time.sleep(1)
