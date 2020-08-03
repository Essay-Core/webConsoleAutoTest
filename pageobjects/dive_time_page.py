#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import unittest
import time
from framework.base_page import BasePage
class Set_time(BasePage):

    time = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/div/input"
    nowBt = 'xpath=>/html/body/div[3]/div[2]/button[1]'
    confirmBt = 'xpath=>/html/body/div[3]/div[2]/button[2]'
    setBt = 'xpath=>//*[@id="app"]/section/section/main/div/div[2]/div[3]/div[1]/div[1]/div/button'
    result_success = 'body > div.el-message.el-message--success.el-message-fade-leave-active.el-message-fade-leave-to > p'

    ntp_sync_checkBox = 'xpath=>//*[@id="app"]/section/section/main/div/div[2]/div[5]/div[2]/div[2]/form/div[1]/div/label/span/span'
    ntp_server_ip = 'xpath=>//input'
    ntp_server_port = 'xpath=>//input'
    ntp_sync_time = 'xpath=>//input'
    ntp_save = 'xpath=>//button[@class="el-button resetBtn el-button--text"]'

    def send_time(self):
        self.clicks(self.time)
        time.sleep(1)
        self.clicks(self.nowBt)
        time.sleep(1)
        self.clicks(self.confirmBt)#查找元素出错err
        time.sleep(1)

    def set_time(self):
        self.clicks(self.setBt)
        time.sleep(1)

    def sync_save(self):
        self.clicks(self.ntp_save)
        time.sleep(1)

