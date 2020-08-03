#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from framework.base_page import BasePage
import time

class BCBBandManage(BasePage):#参数均为bcb基带板参数，如需测试cx基带板，请补充

    refresh = "xpan=>//*[@id='app']/section/section/main/div/div[2]/div[4]/div[1]/div/button/span"#刷新
    band_1 = "xpath=>//div[text()='1']"#列表中第1块基带板
    band_2 = "xpath=>//div[text()='2']"#列表中第2块基带板
    reboot_band = "xpath=>//span[text()='软重启']"
    reboot_shutdown_band = "xpath=>//span[text()='断电重启']"
    not_online_band = "xpath=>//span[text()='离线']"#在线状态
    online_band = "xpath=>//span[text()='在线']"#在线状态
    update_band = "xpath=>//span[text()='固件升级']"
    setpar_band = "xpath=>//span[text()='参数设置']"
    rescan_band = "xpath=>//span[text()='扫网']"
    export_log = "xpath=>//span[text()='导出日志']"
    comfirm = "xpath=>/html/body/div[4]/div/div[3]/button[2]/span"  # 确认
    cancel = "xpath=>/html/body/div[4]/div/div[3]/button[1]/span"   # 取消
    cellid = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[4]/div/div[2]/form/div[2]/div[1]/div/div/div/div/input"
    plmn = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[4]/div/div[2]/form/div[2]/div[2]/div/div/div/div/button"
    mcc_1 = "xpath=>/html/body/div[5]/div/div[2]/form/div[1]/div/div/div/input"
    mcc_2 = "xpath=>/html/body/div[6]/div/div[2]/form/div[1]/div/div/div[1]/input"
    save_plmn = "xpath=>//span[text()='保存']"

    # choice_mcc = "xpath=>//span[text()='中国']"

    mnc = "xpath=>//div[@class='el-select__tags']"
    # choice_mnc ="xpath=>//span[text()='[01] 联通']"

    cancel_plmn = "xpath=>/html/body/div[6]/div/div[3]/div/button[1]"
    bandwidth = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[4]/div/div[2]/form/div[3]/div[1]/div/div/div/div[1]/input"
    bandwidth_20M = "xpath=>//span[text()='20M']"
    bandwidth_15M = "xpath=>//span[text()='15M']"
    bandwidth_10M = "xpath=>//span[text()='10M']"
    bandwidth_5M = "xpath=>//span[text()='5M']"
    arfcn = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[4]/div/div[2]/form/div[3]/div[2]/div/div/div/div/input"
    pci = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[4]/div/div[2]/form/div[3]/div[3]/div/div/div/div/input"
    tac = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[4]/div/div[2]/form/div[4]/div/div/div/div/div/input"
    workmode = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[4]/div/div[2]/form/div[7]/div[1]/div/div/div/div/input"
    workmode_1 = "xpath=>//span[text()='周期侦码模式']"
    workmode_0 = "xpath=>//span[text()='持续侦码模式']"
    capture_time = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[4]/div/div[2]/form/div[7]/div[2]/div/div/div/div/input"#捕获周期
    ifscan_all = 'xpath=>//*[@id="app"]/section/section/main/div/div[2]/div[3]/div[4]/div/div[2]/form/div[10]/div[3]/div/div/div/div/span/span/i'#全频段扫频
    scan_all = "xpath=>//span[text()='启用']"#启用全频段扫频
    unscan_all = "xpath=>//span[text()='禁用']"#禁用全频段扫频
    scan_list = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[4]/div/div[2]/form/div[11]/div/div/div/div/input"#扫频频点列表
    rxgain = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[4]/div/div[2]/form/div[13]/div[1]/div/div/div/div/input"#接收增益
    UePMax = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[4]/div/div[2]/form/div[13]/div[2]/div/div/div/div/input"#输出功率
    rejectCause = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[4]/div/div[2]/form/div[13]/div[3]/div/div/div/div[1]/input"#拒绝原因值
    reject_Cause13="xpath=>//span[text()='CAUSE13']"#CAUSE13
    reject_Cause15 = "xpath=>//span[text()='追踪区域不允许接入']"#追踪区域不允许接入
    reject_Cause12 = "xpath=>//span[text()='追踪区域无适合小区']"#追踪区域无适合小区
    reject_Cause3 = "xpath=>//span[text()='无效终端']"#无效终端
    reject_Cause22 = "xpath=>//span[text()='CAUSE22']"#CAUSE22
    activate_cell = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[4]/div/div[2]/form/div[14]/div[1]/div/div/div/div[1]/input"#启动后自动激活小区
    activate_cell_off = "xpath=>//span[text()='否']"
    activate_cell_on = "xpath=>//span[text()='是']"
    imei_catch = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[4]/div/div[2]/form/div[14]/div[2]/div/div/div/div[1]/input"#IMEI捕获功能
    imei_catch_on = "xpath=>//span[text()='开启']"
    imei_catch_off = "xpath=>//span[text()='关闭']"
    UlPowerAlpha = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[4]/div/div[2]/form/div[14]/div[3]/div/div/div/div[1]/input"#上行功控Alpha系数
    UlPowerAlpha_100 = "xpath=>//span[text()='100']"
    UlPowerAlpha_90 = "xpath=>//span[text()='90']"
    UlPowerAlpha_80 = "xpath=>//span[text()='80']"
    UlPowerAlpha_70 = "xpath=>//span[text()='70']"
    UlPowerAlpha_60 = "xpath=>//span[text()='60']"
    UlPowerAlpha_50 = "xpath=>//span[text()='50']"
    UlPowerAlpha_40 = "xpath=>//span[text()='40']"
    UlPowerAlpha_0 = "xpath=>//span[text()='0']"
    scan_port = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[4]/div/div[2]/form/div[13]/div[1]/div/div/div/div[1]/input"#扫频端口(TDD有效)
    scan_port_sinnifer = "xpath=>//span[text()='SINNIFER端口']"
    scan_port_rx = "xpath=>//span[text()='RX端口']"
    sync_mode = "xpath=>//*[@id='app']/section/section/main/div/div[2]/div[3]/div[4]/div/div[2]/form/div[10]/div[1]/div/div/div/div[1]/input"#同步方式
    sync_gap = "xpath=>//span[text()='空口同步']"
    sync_gps="xpath=>//span[text()='GPS同步']"
    export_par = "xpath=>//span[text()='导出参数']"
    import_par = "xpath=>//span[text()='导入参数']"
    refresh_par = "xpath=>//span[text()='重载参数']"
    cancel_par = "xpath=>//span[text()='取 消']"
    save_par = "xpath=>//span[text()='保存参数']"
    comfirm_save_par = "xpath=>/html/body/div[10]/div/div[3]/button[2]"#确认保存参数
    comfirm_export_par = "xpath=>/html/body/div[7]/div/div[3]/button[2]"#确认导出参数
    cancel_export_par = "xpath=>/html/body/div[7]/div/div[3]/button[1]"#取消导出参数
    choice_par_file = "xpath=>//span[text()='选取文件']"
    cancel_import_par = "xpath=>/html/body/div[7]/div/div[3]/button[1]"#取消导入参数
    update_par_file = "xpath=>//span[text()='上传']"

    #点击刷新按钮
    def click_refresh(self):
        self.clicks(self.refresh)
        time.sleep(1)

    #点击第一块基带板
    def click_band_1(self):
        self.clicks(self.band_1)
        time.sleep(1)

    # 点击第2块基带板
    def click_band_2(self):
        self.clicks(self.band_2)
        time.sleep(1)

    #软重启基带板
    def click_reboot_band(self):
        self.clicks(self.reboot_band)
        time.sleep(1)
        self.clicks(self.comfirm)
        time.sleep(5)

    # 断电重启基带板
    def click_reboot_shutdown_band(self):
        self.clicks(self.reboot_shutdown_band)
        time.sleep(1)
        self.clicks(self.comfirm)
        time.sleep(5)

    #固件升级
    def click_update_band(self):
        self.clicks(self.update_band)
        time.sleep(1)

    #扫网
    def click_rescan(self):
        self.clicks(self.rescan_band)
        time.sleep(1)
        self.clicks(self.comfirm)
        time.sleep(1)

    #导出日志
    def click_export_band_log(self):
        self.clicks(self.export_log)
        time.sleep(1)
        self.clicks(self.comfirm)
        time.sleep(8)

    #弹出框确认键
    def click_comfirm(self):
        self.clicks(self.comfirm)
        time.sleep(1)

    #弹出框取消键
    def click_cancel(self):
        self.clicks(self.cancel)
        time.sleep(1)

    #点击参数设置
    def click_setpar_band(self):
        self.clicks(self.setpar_band)
        time.sleep(1)

    #清空并输入小区id
    def type_cellid(self,text):
        self.clearText(self.cellid)
        self.inputText(self.cellid, text)

    #设置mcc mnc(1)
    def set_plnm(self, mcc_text, mnc_text):
        choice_mcc = "xpath=>//span[text()='" + mcc_text + "']"#中国
        choice_mnc = "xpath=>//span[text()='"+ mnc_text + "']"#[01] 联通
        self.clicks(self.plmn)
        time.sleep(1)
        # self.clicks(self.mcc_1)
        # time.sleep(1)
        # self.clicks(choice_mcc)
        time.sleep(1)
        self.clicks(self.mnc)
        time.sleep(1)
        self.clicks(choice_mnc)
        time.sleep(1)
        self.clicks(self.mnc)
        time.sleep(1)
        self.clicks(self.save_plmn)
        time.sleep(3)


    #带宽选择20m
    def choice_bandwidth_20(self):
        self.clicks(self.bandwidth)
        time.sleep(1)
        self.clicks(self.bandwidth_20M)
        time.sleep(1)

    # 带宽选择15
    def choice_bandwidth_15(self):
        self.clicks(self.bandwidth)
        time.sleep(1)
        self.clicks(self.bandwidth_15M)
        time.sleep(1)
    # 带宽选择10
    def choice_bandwidth_10(self):
        self.clicks(self.bandwidth)
        time.sleep(1)
        self.clicks(self.bandwidth_10M)
        time.sleep(1)
    # 带宽选择5
    def choice_bandwidth_5(self):
        self.clicks(self.bandwidth)
        time.sleep(1)
        self.clicks(self.bandwidth_5M)
        time.sleep(1)

    #清空并输入频点
    def type_arfcn(self,text):
        self.clearText(self.arfcn)
        self.inputText(self.arfcn, text)

    #清空并输入pci
    def type_pci(self,text):
        self.clearText(self.pci)
        self.inputText(self.pci, text)

    #清空并输入tac
    def type_tac(self,text):
        self.clearText(self.tac)
        self.inputText(self.tac, text)

    #选择工作模式：周期侦码
    def choice_workmode_1(self):
        self.clicks(self.workmode)
        time.sleep(1)
        self.clicks(self.workmode_1)
        time.sleep(1)

    #清空并输入捕获周期(分钟)
    def type_capture_time(self,text):
        self.clearText(self.capture_time)
        self.inputText(self.capture_time, text)

    #启用全频段扫频
    def choice_scan_all(self):
        self.clicks(self.ifscan_all)
        time.sleep(2)
        self.clicks(self.scan_all)
        time.sleep(1)

    #禁用全频段扫频
    def choice_unscan_all(self):
        self.clicks(self.ifscan_all)
        time.sleep(1)
        self.clicks(self.unscan_all)
        time.sleep(1)

    #清空并输入扫频频点
    def type_scan_list(self,text):
        self.clearText(self.scan_list)
        self.inputText(self.scan_list, text)

    # 清空并输入接收增益
    def type_rxgain(self,text):
        self.clearText(self.rxgain)
        self.inputText(self.rxgain, text)

    #清空并输入输出功率(dBm)
    def type_UePMax(self,text):
        self.clearText(self.UePMax)
        self.inputText(self.UePMax, text)

    #选择拒绝原因值：cause13
    def choice_reject_cause_13(self):
        self.clicks(self.rejectCause)
        time.sleep(1)
        self.clicks(self.reject_Cause13)
        time.sleep(1)

    #选择拒绝原因值：cause15
    def choice_reject_cause_15(self):
        self.clicks(self.rejectCause)
        time.sleep(1)
        self.clicks(self.reject_Cause15)
        time.sleep(1)

    #选择拒绝原因值：cause12
    def choice_reject_cause_12(self):
        self.clicks(self.rejectCause)
        time.sleep(1)
        self.clicks(self.reject_Cause12)
        time.sleep(1)

    #选择拒绝原因值：cause3
    def choice_reject_cause_3(self):
        self.clicks(self.rejectCause)
        time.sleep(1)
        self.clicks(self.reject_Cause3)
        time.sleep(1)

    #选择拒绝原因值：cause22
    def choice_reject_cause_22(self):
        self.clicks(self.rejectCause)
        time.sleep(1)
        self.clicks(self.reject_Cause22)
        time.sleep(1)

    #启用后自动激活小区
    def choice_activate_cell_on(self):
        self.clicks(self.activate_cell)
        time.sleep(1)
        self.clicks(self.activate_cell_on)
        time.sleep(1)

    #不启用自动激活小区
    def choice_activate_cell_off(self):
        self.clicks(self.activate_cell)
        time.sleep(1)
        self.clicks(self.activate_cell_off)
        time.sleep(1)

    #开启imei捕获功能
    def choice_imei_catch_on(self):
        self.clicks(self.imei_catch)
        time.sleep(1)
        self.clicks(self.imei_catch_on)
        time.sleep(1)

    #关闭imei捕获功能
    def choice_imei_catch_off(self):
        self.clicks(self.imei_catch)
        time.sleep(1)
        self.clicks(self.imei_catch_off)
        time.sleep(1)

    #上行功控Alpha系数:100
    def choice_UlPowerAlpha_100(self):
        self.clicks(self.UlPowerAlpha)
        time.sleep(1)
        self.clicks(self.UlPowerAlpha_100)
        time.sleep(1)

    #上行功控Alpha系数:90
    def choice_UlPowerAlpha_90(self):
        self.clicks(self.UlPowerAlpha)
        time.sleep(1)
        self.clicks(self.UlPowerAlpha_90)
        time.sleep(1)

    #上行功控Alpha系数:80
    def choice_UlPowerAlpha_80(self):
        self.clicks(self.UlPowerAlpha)
        time.sleep(1)
        self.clicks(self.UlPowerAlpha_80)
        time.sleep(1)
    #上行功控Alpha系数:70
    def choice_UlPowerAlpha_70(self):
        self.clicks(self.UlPowerAlpha)
        time.sleep(1)
        self.clicks(self.UlPowerAlpha_70)
        time.sleep(1)
    #上行功控Alpha系数:60
    def choice_UlPowerAlpha_60(self):
        self.clicks(self.UlPowerAlpha)
        time.sleep(1)
        self.clicks(self.UlPowerAlpha_60)
        time.sleep(1)
    #上行功控Alpha系数:50
    def choice_UlPowerAlpha_50(self):
        self.clicks(self.UlPowerAlpha)
        time.sleep(1)
        self.clicks(self.UlPowerAlpha_50)
        time.sleep(1)
    #上行功控Alpha系数:40
    def choice_UlPowerAlpha_40(self):
        self.clicks(self.UlPowerAlpha)
        time.sleep(1)
        self.clicks(self.UlPowerAlpha_40)
        time.sleep(1)
    #上行功控Alpha系数:0
    def choice_UlPowerAlpha_0(self):
        self.clicks(self.UlPowerAlpha)
        time.sleep(1)
        self.clicks(self.UlPowerAlpha_0)
        time.sleep(1)

    #扫频端口(TDD有效):SINNIFER端口
    def choice_scan_port_sinnifer(self):
        self.clicks(self.scan_port)
        time.sleep(1)
        self.clicks(self.scan_port_sinnifer)
        time.sleep(1)

    #扫频端口(TDD有效):RX端口
    def choice_scan_port_rx(self):
        self.clicks(self.scan_port)
        time.sleep(1)
        self.clicks(self.scan_port_rx)
        time.sleep(1)

    #tdd基带板同步方式:空口同步
    def choice_sync_mode_gap(self):
        self.clicks(self.sync_mode)
        time.sleep(1)
        self.clicks(self.sync_gap)
        time.sleep(1)

    #Tdd基带板同步方式:GPS
    def choice_sync_mode_gps(self):
        self.clicks(self.sync_mode)
        time.sleep(1)
        self.clicks(self.sync_gps)
        time.sleep(1)

    #导出核心板参数
    def export_par_file(self):
        self.clicks(self.export_par)
        time.sleep(1)
        self.clicks(self.comfirm_export_par)
        time.sleep(2)

    #取消导出核心板参数
    def cancel_par_file_export(self):
        self.clicks(self.export_par)
        time.sleep(1)
        self.clicks(self.cancel_export_par)
        time.sleep(2)

    #重载参数
    def click_refresh_par(self):
        self.clicks(self.refresh_par)

    #取消导入参数
    def cancel_import_par_file(self):
        self.clicks(self.import_par)
        time.sleep(1)
        self.clicks(self.cancel_import_par)

    #保存参数
    def click_save_par(self):
        self.clicks(self.save_par)

    #取消保存参数
    def click_cancel_par(self):
        self.clicks(self.cancel_par)

    box_confirm = 'xpath=>//button[@class="el-button el-button--default el-button--small el-button--primary "]'
    def click_box_confirm(self):
        self.clicks(self.box_confirm)




























