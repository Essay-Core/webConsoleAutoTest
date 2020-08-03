#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
from framework.base_page import BasePage

class User(BasePage):
    add_user = "xpath=>//span[text()='添加用户']"
    dele_a = "xpath=>//span[text()='批量删除']"
    refresh = 'xpath=>//*[@id="app"]/section/section/main/div/div[2]/div[3]/div/div[1]/div/button[3]/span'
    user = 'xpath=>//*[@id="app"]/section/section/main/div/div[2]/div[3]/div/div[4]/div/div[2]/form/div[1]/div/div/input'
    name = 'xpath=>//*[@id="app"]/section/section/main/div/div[2]/div[3]/div/div[4]/div/div[2]/form/div[2]/div/div/input'
    passwd = 'xpath=>//*[@id="app"]/section/section/main/div/div[2]/div[3]/div/div[4]/div/div[2]/form/div[3]/div/div/input'
    passwd_c = 'xpath=>//*[@id="app"]/section/section/main/div/div[2]/div[3]/div/div[4]/div/div[2]/form/div[4]/div/div/input'
    static = 'xpath=>//*[@id="app"]/section/section/main/div/div[2]/div[3]/div/div[4]/div/div[2]/form/div[5]/div/div/div[1]/input'
    remark = 'xpath=>//*[@id="app"]/section/section/main/div/div[2]/div[3]/div/div[4]/div/div[2]/form/div[6]/div/div/textarea'
    static_no = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[1]"
    #static_on = "xpath=>/html/body/div[6]/div[1]/div[1]/ul/li[1]"
    static_on = 'div.el-select-dropdown.el-popper > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li.el-select-dropdown__item.selected'
    static_off = "xpath=>//span[text()='禁用']"

    confirm = "xpath=>//span[text()='确 定']"
    cancel = "xpath=>//span[text()='取 消']"
    confirm_alart = "xpath=>/html/body/div[4]/div/div[3]/button"
    body = 'body'
    err_confirm = 'div.el-message-box__wrapper > div > div.el-message-box__btns > button'
    flags = False
    def click_add(self):
        self.clicks(self.add_user)
        time.sleep(1)

    def add(self,user,name,passwd,passwd_c,remark):
        self.inputText(self.user, user)
        self.inputText(self.name, name)
        self.inputText(self.passwd, passwd)
        self.inputText(self.passwd_c, passwd_c)

        time.sleep(1)
        if self.flags == False:
            self.clicks(self.static)
            time.sleep(1)
            self.clicks(self.static_no)     #启用状态
            #self.clicks(self.static_off)   #禁用状态
            self.flags = True
        time.sleep(1)
        self.inputText(self.remark, remark)
        time.sleep(1)
        self.clicks(self.confirm)

    def click_sub(self,body,sub):
        p = self.driver.find_element_by_css_selector(body)
        p.find_element_by_css_selector(sub).click()
        time.sleep(1)

    def click_err_confirm(self,driver):
        time.sleep(1)
        p = driver.find_element_by_css_selector(self.body)
        p.find_element_by_css_selector(self.err_confirm).click()
        time.sleep(1)