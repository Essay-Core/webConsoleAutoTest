#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from framework.base_page import BasePage

class zmDataPage(BasePage):
    zmgl = "xpath=>//span[text()='侦码管理']"
    zmdata = "xpath=>//span[text()='侦码数据']"
    starttime = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[1]/div/div[1]/input[1]"#开始时间
    endtime = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[1]/div/div[1]/input[2]"#结束时间
    weektime = "xpath=>//button[text()='最近一周']"
    amontime = "xpath=>//button[text()='最近一个月']"
    thrmontime = "xpath=>//button[text()='最近三个月']"
    iffilt = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[1]/div/label/span[1]"#去重查询
    imsi = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[1]/div/div[2]/input"#输入 imsi
    select = "xpath=>//span[text()='查询']"
    exportExc = "xpath=>//span[text()='导出excel']"
    refresh = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[1]/div/button[2]"#刷新
    comfirm = "xpath=>/html/body/div[4]/div/div[3]/button[2]/span"#确认导出

    def open_zmgl(self):
        self.clicks(self.zmgl)

    def outcomfirm(self):
        self.clicks(self.comfirm)

    def open_zmdata(self):
        self.clicks(self.zmdata)

    def chioce_startime(self):
        self.clicks(self.starttime)

    def chioce_endtime(self):
        self.clicks(self.endtime)

    def chioce_week(self):
        self.clicks(self.weektime)

    def chioce_mon(self):
        self.clicks(self.amontime)

    def chioce_thrmon(self):
        self.clicks(self.thrmontime)

    def selectImsidate(self):
        self.clicks(self.select)

    def send_refresh(self):
        self.clicks(self.refresh)

    def exportData(self):
        self.clicks(self.exportExc)

    def filt(self):
        self.clicks(self.iffilt)

