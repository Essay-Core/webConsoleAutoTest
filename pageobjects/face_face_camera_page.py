#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from framework.base_page import BasePage
import time

class FACE(BasePage):

    add_camera_btn = "xpath=>//span[text()='添加人脸摄像机']"
    refresh = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[5]/div/div[1]/div/button[2]/span"
    camera_ip = "xpath=>//input[@placeholder='请输入正确摄像机ip地址']"
    camera_id = "xpath=>//input[@placeholder='摄像机id号不可重复']"
    camera_port = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div/div[3]/div/div[2]/form/div[2]/div/div/div/input"
    camera_user = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div/div[3]/div/div[2]/form/div[3]/div/div/input"
    camera_passwd = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div/div[3]/div/div[2]/form/div[4]/div/div/input"
    camera_confirm = "xpath=>//span[text()='确 定']"
    confirm = 'xpath=>/html/body/div[3]/div/div[3]/button/span'
    camera_cancel = "xpath=>//span[text()='取 消']"
    camera_close = "xpath=>//i[@class='el-dialog__close el-icon el-icon-close']"  #关闭
    #//*[@id="app"]/section/section/main/div/div[2]/div[3]/div/div[3]/div/div[1]/button/i
    #<i class="el-dialog__close el-icon el-icon-close"></i>
    #//*[@id="app"]/section/section/main/div/div[2]/div[6]/div/div[1]/div/button[2]/span


    def add_camera1(self,camera_ip,camera_port,camera_user,camera_passwd,camera_id):
        self.clicks(self.add_camera_btn)
        time.sleep(1)
        self.inputText(self.camera_ip, camera_ip)
        self.inputText(self.camera_port, camera_port)
        self.inputText(self.camera_user, camera_user)
        self.inputText(self.camera_passwd, camera_passwd)
        self.inputText(self.camera_id, camera_id)
        self.clicks(self.camera_close)


    def add_camera2(self,camera_ip):
        self.clicks(self.add_camera_btn)
        time.sleep(1)

    #点击添加摄像机
    def click_add_camera(self):
        self.clicks(self.add_camera_btn)
        time.sleep(1)

    # 点击添加摄像机
    def input_add_message(self,camera_ip,camera_port,camera_user,camera_passwd,camera_id):
        self.inputText(self.camera_ip, camera_ip)
        self.inputText(self.camera_port, camera_port)
        self.inputText(self.camera_user, camera_user)
        self.inputText(self.camera_passwd, camera_passwd)
        self.inputText(self.camera_id, camera_id)
        self.clicks(self.camera_confirm)
        time.sleep(1)

    def click_confirm(self):
        self.clicks(self.confirm)
        time.sleep(1)


