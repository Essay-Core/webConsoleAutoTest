from framework.base_page import BasePage
import time

class Plate_server(BasePage):
    mcb_id = 'xpath=>//input[@placeholder="请输入贴纸标签的设备编号"]'
    server_ip = 'xpath=>//input[@placeholder="请输入服务器ip地址"]'
    server_port = 'xpath=>//input[@role="spinbutton"]'
    confirm = 'xpath=>//button[@class="el-button resetBtn el-button--primary"]'
    reflash = 'xpath=>//button[@text()="刷新"]'
    box_confirm = 'xpath=>//button[@class="el-button el-button--default el-button--small el-button--primary "]'

    def input_server_messgae(self,id, ip, port):
        self.inputText(self.mcb_id, id)
        self.inputText(self.server_ip, ip)
        self.inputText(self.server_port, port)
        time.sleep(1)
        self.clicks(self.confirm)

    def click_confirm(self):
        time.sleep(1)
        self.clicks(self.box_confirm)
