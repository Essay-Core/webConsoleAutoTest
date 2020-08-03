#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from framework.base_page import BasePage
import time

class FACE_server(BasePage):
    band_id = "xpath=>//input[@placeholder='请输入设备编号']"
    server_ip = "xpath=>//input[@placeholder='请输入服务器ip地址']"
    server_port = 'xpath=>//*[@id="app"]/section/section/main/div/div[2]/div[3]/div/div/form/div[3]/div/div/div/input'
    confirm = "xpath=>//span[text()='确 定']"
    cancel = "xpath=>//span[text()='刷 新']"

    def set_par(self,band_id,server_ip,server_port):
        self.clearText(self.band_id)
        self.inputText(self.band_id, band_id)
        self.clearText(self.server_ip)
        self.inputText(self.server_ip, server_ip)
        self.clearText(self.server_port)
        self.inputText(self.server_port, server_port)
        self.clicks(self.confirm)
        time.sleep(1)

    def click_close(self):
        self.clicks(self.close)
        time.sleep(1)


