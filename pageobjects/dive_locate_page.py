#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import unittest
import time
from framework.base_page import BasePage
class Set_locate(BasePage):

    longitudeEd = 'xpath=>//input[@placeholder="经度"]'
    latitudeEd = 'xpath=>//input[@placeholder="纬度"]'
    saveBt = 'xpath=>//button[@class="el-button el-button--text"]'
    errConfirm = 'xpath=>//button[@class="el-button el-button--default el-button--small el-button--primary "]'

    def set_message(self,longitude,latitude):
        self.inputText(self.longitudeEd,longitude)
        self.inputText(self.latitudeEd, latitude)
        time.sleep(1)

    def save(self):
        self.clicks(self.saveBt)
        time.sleep(1)

    def clicks_errconfirm(self):
        self.clicks(self.errConfirm)
        time.sleep(1)

