#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from framework.base_page import BasePage

class zmServerpage(BasePage):
    zmgl = "xpath=>//span[text()='侦码管理']"
    zmgl_server = "xpath=>//span[text()='服务器配置']"
    imsi_filtration_time = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div/div[2]/form/div[2]/div/div/div/input"
    main_server_ip = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div/div[2]/form/div[4]/div/div/input"
    main_server_port = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div/div[2]/form/div[5]/div/div/div/input"
    if_second_server = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div/div[2]/form/div[7]/div/label/span/span"
    second_server_ip = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div/div[2]/form/div[9]/div/div/input"
    second_server_port = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div/div[2]/form/div[10]/div/div/div/input"
    save_par = "xpath=>//span[text()='保存']"
    main_ping = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div/div[2]/form/div[4]/div/div/div/button"
    sec_ping = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div/div[2]/form/div[9]/div/div/div/button"
    errConfirm = 'xpath=>//button[@class="el-button el-button--default el-button--small el-button--primary "]'
    def pingMain(self):
        self.clicks(self.main_ping)
    def pingSec(self):
        self.clicks(self.sec_ping)

    def open_zmgl(self):
        self.clicks(self.zmgl)

    def open_zmServer(self):
        self.clicks(self.zmgl_server)

    def setSec(self):
        self.clicks(self.if_second_server)

    def type_imsiFilTime(self,text):
        self.inputText(self.imsi_filtration_time, text)
    def clearFtime(self):
        self.clearText(self.imsi_filtration_time)

    def type_mainSerIP(self,text):
        self.inputText(self.main_server_ip, text)
    def clearMserIP(self):
        self.clearText(self.main_server_ip)

    def type_mainSerPort(self,text):
        self.inputText(self.main_server_port, text)
    def clearMserPort(self):
        self.clearText(self.main_server_port)

    def type_secSerIP(self,text):
        self.inputText(self.second_server_ip, text)
    def clearSecIP(self):
        self.clearText(self.second_server_ip)

    def type_secSerPort(self,text):
        self.inputText(self.second_server_port, text)
    def clearSecport(self):
        self.clearText(self.second_server_port)

    def saveSerPar(self):
        self.clicks(self.save_par)

    def clicks_errconfirm(self):
        self.clicks(self.errConfirm)

