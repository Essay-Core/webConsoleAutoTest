#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
from framework.base_page import BasePage

class PASSWD(BasePage):
    old_passwd = 'xpath=>//*[@id="app"]/section/section/main/div/div[2]/div[3]/div/div/form/div[2]/div/div/input'
    new_passwd = 'xpath=>//*[@id="app"]/section/section/main/div/div[2]/div[3]/div/div/form/div[3]/div/div/input'
    new_passwd_2 = 'xpath=>//*[@id="app"]/section/section/main/div/div[2]/div[3]/div/div/form/div[4]/div/div/input'
    save_passwd = 'xpath=>//*[@id="app"]/section/section/main/div/div[2]/div[3]/div/div/form/div[5]/div/button'
    confirm_alart = 'xpath=>/html/body/div[3]/div/div[3]/button'
    body = 'body'
    err_confirm = 'div.el-message-box__wrapper > div > div.el-message-box__btns > button'

    def update_passwd(self,old_passwd,new_passwd,new_passwd_2):
        self.inputText(self.old_passwd, old_passwd)
        self.inputText(self.new_passwd, new_passwd)
        self.inputText(self.new_passwd_2, new_passwd_2)
        time.sleep(1)
        self.clicks(self.save_passwd)
        time.sleep(1)

    def click_err_confirm(self,driver):
        time.sleep(1)
        p = driver.find_element_by_css_selector(self.body)
        p.find_element_by_css_selector(self.err_confirm).click()
        time.sleep(1)
