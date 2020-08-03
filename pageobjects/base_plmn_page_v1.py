#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import unittest
import time
from framework.base_page import BasePage



class Set_plmn(BasePage):
    #add_mcc = 'xpath=>//*[@id="app"]/section/section/main/div/div[2]/div[3]/div/div[1]/button'
    add_mcc = 'xpath=>(//button[@class="el-button el-button--success is-plain"])[1]'
    mcc = 'xpath=>//input[@placeholder="请输入MCC"]'
    national_regional_code = "xpath=>//input[@placeholder='请输入国家/区域']"
    mcc_save = 'xpath=>//i[@class="el-icon-folder"]'
    mcc_cancel = 'xpath=>/html/body/div[6]/div/div[3]/div/button[1]'

    add_mnc = 'xpath=>//span[contains(text(),"添加MNC")]'
    mnc = 'xpath=>(//input[@placeholder="请输入MNC"])'
    carrieroperator = 'xpath=>//input[@placeholder="请输入运营商"]'
    standard_tdd_lte = 'xpath=>/html/body/div[4]/div/div[2]/form/div[4]/div/div/label[1]/span[1]/span'
    mnc_save = 'xpath=>(//button[@class="el-button el-button--primary el-button--medium"])[1]'
    mnc_cancel = ''

    err_confirm = 'xpath=>//button[@class="el-button el-button--default el-button--small el-button--primary "]'

    def click_add_mcc(self):
        time.sleep(1)
        self.clicks(self.add_mcc)
        time.sleep(1)

    def input_mcc(self,mcc,national_code):
        self.inputText(self.mcc, mcc)
        self.inputText(self.national_regional_code, national_code)
        time.sleep(1)
        print("button save")
        self.clicks(self.mcc_save)
        time.sleep(1)

    def click_add_mnc(self):
        self.clicks(self.add_mnc)
        time.sleep(1)

    def input_mnc(self,mnc,carrier):
        self.inputText(self.mnc,mnc)
        self.inputText(self.carrieroperator,carrier)
        self.clicks(self.mnc_save)
        time.sleep(1)


    def click_err_confirm(self):
        time.sleep(1)
        self.clicks(self.err_confirm)
        time.sleep(1)

    def click_standard(self):
        time.sleep(1)
        self.clicks(self.standard_tdd_lte)



