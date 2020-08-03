#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from framework.base_page import BasePage
import time

class Rtime_imsi(BasePage):
    add_imsi = "xpath=>//span[text()='新增']"
    delet_imsi = "xpath=>//span[text()='删除']"
    confirm_del = 'xpath=>/html/body/div[3]/div/div[3]/button[2]/span'
    cancel_del = 'xpath=>/html/body/div[3]/div/div[3]/button[1]/span'
    refresh_imsi = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[1]/div/button[3]/span"#刷新
    import_imsi = "xpath=>//span[text()='导入excel']"
    down_imsimode = "xpath=>//span[text()='下载模板']"
    # type_imsi = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[5]/div[3]/div/div[2]/form/div[1]/div/label[1]/span[1]/span"
    type_imsi = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[3]/div/div[2]/form/div[1]/div/label[1]/span[1]/span"
    imsi_text = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[3]/div/div[2]/form/div[2]/div/div/input"
    confirm = "xpath=>//span[text()='确 定']"
    all_imsi = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[2]/div[2]/table/thead/tr/th[1]/div/label/span"#全选

    def refresh_list(self):
        self.clicks(self.refresh_imsi)

    def add_imsi_input(self,text):
        self.clicks(self.add_imsi)
        time.sleep(1)
        self.clicks(self.type_imsi)
        self.inputText(self.imsi_text, text)
        time.sleep(1)
        self.clicks(self.confirm)

    def click_add_imsi(self):
        self.clicks(self.add_imsi)
        time.sleep(1)

    def input_imsi(self,text):
        self.clicks(self.type_imsi)
        self.inputText(self.imsi_text, text)
        time.sleep(1)
        self.clicks(self.confirm)

    def choice_all_imsi(self,driver):
        main_path = '#app > section > section > main'
        sub_path = 'main > div > div.el-tabs__content > div.box-card > div.el-table.el-table--fit.el-table--enable-row-hover.el-table--enable-row-transition > div.el-table__header-wrapper > table > thead > tr > th.el-table_1_column_1.el-table-column--selection.is-leaf > div > label > span'
        find = driver.find_element_by_css_selector(main_path)
        find.find_element_by_css_selector(sub_path).click()
        time.sleep(1)

    def click_err_confirm(self,driver):
        main_path = 'body > div.el-message-box__wrapper > div > div.el-message-box__btns > button'
        sub_path = ''
        driver.find_element_by_css_selector(main_path).click()
        time.sleep(1)

    def delete_imsi(self):
        self.clicks(self.delet_imsi)
        time.sleep(1)
        self.clicks(self.confirm_del)
        time.sleep(1)


    def down_modefile(self):
        self.clicks(self.down_imsimode)
        time.sleep(3)
