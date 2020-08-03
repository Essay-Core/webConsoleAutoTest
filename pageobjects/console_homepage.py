#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from framework.base_page import BasePage
import time

class HomePage(BasePage):
    inputuser_box = "xpath=>//input[@placeholder='请输入用户名']"
    inputpasswd_box = "xpath=>//input[@type='password']"
    login_submit_btn = "xpath=>//span[text()='登录']"
    login_fail_e = "xpath=>//p[text()='用户名或密码错误！']"
    login_pass_e = "xpath=>//div[text()='首页']"
    divetime = "xpath=>//span[text()='设备时间']"
    diveplmn = "xpath=>//span[text()='PLMN管理']"
    divelocate = "xpath=>//span[text()='设备位置信息']"
    base_set = "xpath=>//span[text()='基本设置']"
    plmn_manage = "xpath=>//span[text()='PLMN管理']"
    jz_manage = "xpath=>//span[text()='基站管理']"
    band_manage = "xpath=>//span[text()='核心板管理']"
    pa_manage = "xpath=>//span[text()='功放管理']"
    alarm_set = "xpath=>//span[text()='告警设置']"
    zm_manage = "xpath=>//span[text()='侦码管理']"
    imsi_server_manage = "xpath=>//span[text()='服务器配置']"
    imsi_data = "xpath=>//span[text()='侦码数据']"
    real_time_data = "xpath=>//span[text()='实时数据']"
    real_time_imsi = "xpath=>//span[text()='上号筛选目标']"
    filt_imsi_list = "xpath=>//span[text()='上号筛选数据']"
    kb_real_time_elemt = "xpath=>//span[text()='核心板实时参数']"
    real_time_rrc = "xpath=>//span[text()='随机接入成功率']"
    result_scan = "xpath=>//span[text()='扫频结果']"
    kb_temperature = "xpath=>//span[text()='核心板温度']"
    wifi_manage = "xpath=>//span[text()='wifi管理']"
    # wifi_server_manage = "xpath=>//span[text()='服务器配置']"
    wifi_server_manage = "xpath=>//*[@id='app']/section/section/aside/ul/li[5]/ul/li[1]"
    mac_data = "xpath=>//span[text()='Mac信息']"
    virtual_data = 'xpath=>//span[text()="虚拟身份信息"]'
    face = "xpath=>//span[text()='人脸识别']"
    face_camera = "xpath=>//span[text()='人脸摄像机']"
    face_server = "xpath=>//span[text()='人脸平台信息']"
    plate = "xpath=>//span[text()='车牌识别']"
    plate_camera = "xpath=>//span[text()='车牌摄像机']"
    plate_server = "xpath=>//span[text()='车牌服务器配置']"
    system_ctrl = "xpath=>//span[text()='系统控制']"
    user_manage = "xpath=>//span[text()='用户管理']"
    passwd_manage = "xpath=>//span[text()='修改密码']"
    alarm_log = "xpath=>//span[text()='告警日志']"
    download_log = "xpath=>//span[text()='日志下载']"
    route_track = "xpath=>//span[text()='路由追踪']"
    system_update = "xpaht=>//span[text()='软件升级']"
    #




    def type_user(self,text):
        self.inputText(self.inputuser_box, text)

    def type_pwd(self,text):
        self.inputText(self.inputpasswd_box, text)

    def send_login_btn(self):
        self.clicks(self.login_submit_btn)

    def findE(self):
        self.find_element(self.login_fail_e)

    def findP(self):
        self.get_eText(self.login_pass_e)

    def console_login_succ(self):
        consolelogin = HomePage(self.driver)
        consolelogin.type_user("admin")
        consolelogin.type_pwd("123456")
        consolelogin.send_login_btn()

    #打开设备时间页面
    def open_divetime(self):
        self.clicks(self.base_set)
        time.sleep(1)
        self.clicks(self.divetime)
        time.sleep(1)

    #打开plmn管理页面
    def open_plmn(self):
        self.clicks(self.base_set)
        time.sleep(1)
        self.clicks(self.diveplmn)
        time.sleep(1)

    #打开设备位置信息
    def open_divelocate(self):
        self.clicks(self.base_set)
        time.sleep(1)
        self.clicks(self.divelocate)
        time.sleep(1)

    #打开plmn页面
    def open_plmn_manage(self):
        self.clicks(self.base_set)
        time.sleep(1)
        self.clicks(self.plmn_manage)
        time.sleep(1)

    #打开核心板管理
    def open_band_manage(self):
        self.clicks(self.jz_manage)
        time.sleep(1)
        self.clicks(self.band_manage)
        time.sleep(1)

    #打开功放管理
    def open_pa_manage(self):
        self.clicks(self.jz_manage)
        time.sleep(1)
        self.clicks(self.pa_manage)
        time.sleep(1)

    #打开告警设置
    def open_alarm_set(self):
        self.clicks(self.jz_manage)
        time.sleep(1)
        self.clicks(self.alarm_set)
        time.sleep(1)

    #打开IMSI服务器设置
    def open_imsi_server_manage(self):
        self.clicks(self.zm_manage)
        time.sleep(1)
        self.clicks(self.imsi_server_manage)
        time.sleep(1)

    #打开侦码数据
    def open_imsi_data(self):
        self.clicks(self.zm_manage)
        time.sleep(1)
        self.clicks(self.imsi_data)
        time.sleep(1)

    #打开上号筛选目标
    def open_real_time_imsi(self):
        self.clicks(self.real_time_data)
        time.sleep(1)
        self.clicks(self.real_time_imsi)
        time.sleep(1)

    def open_kb_real_time_elemts(self):
        self.clicks(self.real_time_data)
        time.sleep(1)
        self.clicks(self.kb_real_time_elemt)
        time.sleep(1)

    def open_radom_access(self):
        self.clicks(self.real_time_data)
        time.sleep(1)
        self.clicks(self.real_time_rrc)
        time.sleep(1)

    #打开上号筛选数据
    def open_filt_imsi_list(self):
        self.clicks(self.real_time_data)
        time.sleep(1)
        self.clicks(self.filt_imsi_list)
        time.sleep(1)

    #打开随机接入成功率
    def open_real_time_rrc(self):
        self.clicks(self.real_time_data)
        time.sleep(1)
        self.clicks(self.real_time_rrc)
        time.sleep(1)

    #打开扫频结果
    def open_result_scan(self):
        self.clicks(self.real_time_data)
        time.sleep(1)
        self.clicks(self.result_scan)
        time.sleep(1)

    #
    def open_kb_tempera(self):
        self.clicks(self.real_time_data)
        time.sleep(1)
        self.clicks(self.kb_temperature)
        time.sleep(1)

    #打开WiFi服务器管理
    def open_wifi_server_manage(self):
        self.clicks(self.wifi_manage)
        time.sleep(1)
        self.clicks(self.wifi_server_manage)
        time.sleep(1)

    #打开Mac信息
    def open_mac_data(self):
        self.clicks(self.wifi_manage)
        time.sleep(1)
        self.clicks(self.mac_data)
        time.sleep(1)

    #打开虚拟身份
    def open_virtual_data(self):
        self.clicks(self.wifi_manage)
        time.sleep(1)
        self.clicks(self.virtual_data)
        time.sleep(1)

    #打开人脸摄像机
    def open_face_camera(self):
        self.clicks(self.face)
        time.sleep(1)
        self.clicks(self.face_camera)
        time.sleep(1)

    #打开人脸平台信息
    def open_face_server(self):
        self.clicks(self.face)
        time.sleep(1)
        self.clicks(self.face_server)
        time.sleep(1)

    #打开车牌服务器配置
    def open_palte_server(self):
        self.clicks(self.plate)
        time.sleep(1)
        self.clicks(self.plate_server)
        time.sleep(1)

    #打开车牌摄像机
    def open_palte_camera(self):
        self.clicks(self.plate)
        time.sleep(1)
        self.clicks(self.plate_camera)
        time.sleep(1)

    #打开用户管理
    def open_user_manage(self):
        self.clicks(self.system_ctrl)
        time.sleep(1)
        self.clicks(self.user_manage)
        time.sleep(1)

    #打开修改密码
    def open_passwd_manage(self):
        self.clicks(self.system_ctrl)
        time.sleep(1)
        self.clicks(self.passwd_manage)
        time.sleep(1)

    #打开告警日志
    def open_alarm_log(self):
        self.clicks(self.system_ctrl)
        time.sleep(1)
        self.clicks(self.alarm_log)
        time.sleep(1)

    #打开日志下载
    def open_download_log(self):
        self.clicks(self.system_ctrl)
        time.sleep(1)
        self.clicks(self.download_log)
        time.sleep(1)
    #打开路由追踪
    def open_route_track(self):
        self.clicks(self.system_ctrl)
        time.sleep(1)
        self.clicks(self.route_track)
        time.sleep(1)
    #打开软件升级
    def open_system_update(self):
        self.clicks(self.system_ctrl)
        time.sleep(1)
        self.clicks(self.system_update)
        time.sleep(1)

