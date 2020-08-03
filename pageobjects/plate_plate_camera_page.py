from framework.base_page import BasePage
import time

class Plate_camera(BasePage):
    add_plate_camera = 'xpath=>//button[@class="el-button el-button--success is-plain"]'
    camera_ip = 'xpath=>//input[@placeholder="请输入车牌摄像机ip地址"]'
    camera_port = 'xpath=>//input[@max="65535"]'
    camera_user = 'xpath=>//*[@id="app"]/section/section/main/div/div[2]/div[3]/div/div[3]/div/div[2]/form/div[3]/div/div[1]/input'
    camera_passwd = 'xpath=>//*[@id="app"]/section/section/main/div/div[2]/div[3]/div/div[3]/div/div[2]/form/div[4]/div/div[1]/input'
    camera_id = 'xpath=>//input[@placeholder="摄像机id号不可重复"]'
    confirm = 'xpath=>//button[@class="el-button el-button--primary"]'
    box_confirm = 'xpath=>//button[@class="el-button el-button--default el-button--small el-button--primary "]'

    # 点击添加摄像机
    def click_add_camera(self):
        self.clicks(self.add_plate_camera)
        time.sleep(1)

    # 点击添加摄像机
    def input_add_message(self, camera_ip, camera_port, camera_user, camera_passwd, camera_id):
        time.sleep(1)
        self.inputText(self.camera_ip, camera_ip)
        self.inputText(self.camera_port, camera_port)
        self.inputText(self.camera_user, camera_user)
        self.inputText(self.camera_passwd, camera_passwd)
        self.inputText(self.camera_id, camera_id)
        self.clicks(self.confirm)
        time.sleep(1)

    def click_confirm(self):
        self.clicks(self.box_confirm)
        time.sleep(1)
