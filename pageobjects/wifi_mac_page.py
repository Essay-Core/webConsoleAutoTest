#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from framework.base_page import BasePage
import time

class MAC(BasePage):
    start_time = "xpath=>//input[@placeholder='开始日期']"
    time_week = "xpath=>//button[text()='最近一周']"
    time_month = "xpath=>//button[text()='最近一个月']"
    time_month_3 = "xpath=>//button[text()='最近三个月']"
    time_confirm = "xpath=>/html/body/div[4]/div[2]/button[2]/span"#查询时间确认键
    time_clear = "xpath=>/html/body/div[3]/div[2]/button[1]/span"#查询时间清空键
    input_mac = "xpath=>//input[@placeholder='请输入MAC']"
    select_mac = "xpath=>//span[text()='查询']"
    exprot_mac = "xpath=>//span[text()='导出EXCEL']"
    refresh_mac = "xpath=>//span[text()='刷新']"
    confirm_out = "xpath=>/html/body/div[3]/div/div[3]/button"

    def select_time_week(self):
        self.clicks(self.start_time)
        time.sleep(1)
        self.clicks(self.time_week)
        time.sleep(1)
        # self.clicks(self.selet_mac)
        # time.sleep(1)

    def select_time_month(self):
        self.clicks(self.start_time)
        time.sleep(1)
        self.clicks(self.time_month)
        time.sleep(1)
        # self.clicks(self.selet_mac)
        # time.sleep(1)

    def select_time_month_3(self):
        self.clicks(self.start_time)
        time.sleep(1)
        self.clicks(self.time_month_3)
        time.sleep(1)
        # self.clicks(self.selet_mac)
        # time.sleep(1)

    def clear_select_time(self):
        self.clicks(self.start_time)
        time.sleep(1)
        self.clicks(self.time_clear)

    def mac_export(self):
        self.clicks(self.start_time)
        time.sleep(1)
        self.clicks(self.time_month_3)
        time.sleep(2)
        self.clicks(self.exprot_mac)
        time.sleep(1)
        self.clicks(self.confirm_out)

    def click_select(self):
        self.clicks(self.select_mac)

    def clicks_refresh(self):
        self.clicks(self.refresh_mac)

    def type_mac(self,text):
        self.inputText(self.input_mac, text)