#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from framework.base_page import BasePage
import time

class WIFI_server(BasePage):
    save_par = "xpath=>//span[text()='保存']"
    main_serIP = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div/div[2]/form/div[2]/div/div/input"
    main_serPort = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div/div[2]/form/div[3]/div/div/div/input"
    main_ping = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div/div[2]/form/div[2]/div/div/div/button"
    sec_serIP = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/input"
    sec_serPort = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div/div[2]/form/div[7]/div/div/div/input"
    sec_ping = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div/div[2]/form/div[6]/div/div/div/button"
    if_sec = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div/div[2]/form/div[5]/div/label/span/span"#复选框
    confirm = "xpath=>/html/body/div[3]/div/div[3]/button"#确定
    errConfirm = 'xpath=>//button[@class="el-button el-button--default el-button--small el-button--primary "]'

    def click_save(self):
        self.clicks(self.save_par)

    def type_main_ip(self,text):
        self.clearText(self.main_serIP)
        self.inputText(self.main_serIP, text)

    def type_main_port(self,text):
        self.clearText(self.main_serPort)
        self.inputText(self.main_serPort, text)

    def ping_main_ser(self):
        self.clicks(self.main_ping)
        time.sleep(2)
        self.clicks(self.confirm)

    def ping_sec_ser(self):
        self.clicks(self.sec_ping)
        time.sleep(2)
        self.clicks(self.confirm)

    def type_sec_ip(self,text):
        self.clearText(self.sec_serIP)
        self.inputText(self.sec_serIP, text)

    def type_sec_port(self,text):
        self.clearText(self.sec_serPort)
        self.inputText(self.sec_serPort, text)

    def click_if_sec(self):
        self.clicks(self.if_sec)

    def clicks_errconfirm(self):
        self.clicks(self.errConfirm)


