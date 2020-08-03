#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from framework.logger import Logger
import time
import threading
#import openpyxl
#from openpyxl.styles import Alignment,PatternFill,Font
#from openpyxl.utils import get_column_letter
import sys

#获取系统当前时间,不会改变
stime = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
logger = Logger(logger='MyTestV2').getlog()
filename = stime

#单元格颜色填充选项
#red_fill = PatternFill("solid", fgColor="FF0000")
#green_fill = PatternFill("solid", fgColor="00FF00")

#字体格式，颜色和大小
#font_pass = Font(size=16, bold=True, color="00FF00")
#font_false = Font(size=16, bold=True, color="FF0000")

# 先定位主筐体的位置，让后通过相对位置来定位表格中的元素
main_xpath = '//main[@class="el-main main"]'
url = "http://192.168.3.200/#/login"
Chrome_path = "F:\pyaz\chromedriver.exe"
inputuser_box = "//input[@placeholder='请输入用户名']"
inputpasswd_box = "//input[@type='password']"
login_submit_btn = "//*[@id='app']/div/div/form/button"#登录按钮

#主控重启
reboot_mcband = "//*[@id='app']/section/header/div[2]/button[1]"  # 重启系统
comfirm = "/html/body/div[3]/div/div[3]/button[2]/span"#确认

band_1 = "//div[text()='1']"#列表中第1块基带板
band_2 = "//div[text()='2']"#列表中第2块基带板
band_3 = "//div[text()='3']"#列表中第3块基带板

setpar_band = "//span[text()='参数设置']"
UePMax = "//*[@id='app']/section/section/main/div/div[2]/div[3]/div[4]/div/div[2]/form/div[13]/div[2]/div/div/div/div/input"#输出功率
save_par = "//span[text()='保存参数']"
comfirm_button = "//button[@class='el-button el-button--default el-button--small el-button--primary ']"

jz_manage = "//span[text()='基站管理']"
band_manage = "//span[text()='核心板管理']"
pa_manage = "//span[text()='功放管理']"

reboot_band = "//span[text()='软重启']"
comfirm_soft = "/html/body/div[3]/div/div[3]/button[2]/span"
power_outage_restart = "//span[text()='断电重启']"

pa_on = "//span[text()='开启所有功放']"
pa_off = "//span[text()='关闭所有功放']"
refresh = "//i[@class='el-icon-refresh']"

# B40
B40_table_pa_xpath = "//*[@id='app']/section/section/main/div/div[2]/div[3]/div[2]/div[3]/table/tbody/tr[1]/td[9]"
B40_table_pa_css = "#app > section > section > main > div > div.el-tabs__content > div.box-card > div.el-table.el-table--fit.el-table--border.el-table--scrollable-x.el-table--enable-row-hover.el-table--enable-row-transition.el-table--mini > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(1) > td.el-table_1_column_9 > div > div > span"

# 读取B1功放
B1_table_pa_xpath = "//*[@id='app']/section/section/main/div/div[2]/div[3]/div[2]/div[3]/table/tbody/tr[2]/td[9]"
B1_table_pa_css = "#app > section > section > main > div > div.el-tabs__content > div.box-card > div.el-table.el-table--fit.el-table--border.el-table--scrollable-x.el-table--enable-row-hover.el-table--enable-row-transition.el-table--mini > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(2) > td.el-table_1_column_9 > div > div > span"

# 读取gsm功放
GSM_table_pa_xpath = "//*[@id='app']/section/section/main/div/div[2]/div[3]/div[2]/div[3]/table/tbody/tr[3]/td[9]"
GSM_table_pa_css = "#app > section > section > main > div > div.el-tabs__content > div.box-card > div.el-table.el-table--fit.el-table--border.el-table--scrollable-x.el-table--enable-row-hover.el-table--enable-row-transition.el-table--mini > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(3) > td.el-table_1_column_9 > div > div > span"

#核心板: OS：online status ;WS: work status;
#FDD-56
OS_FDD_56_xpath_iframe = '//*[@id="app"]/section/section/main/div/div[2]/div[4]/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/span'
OS_FDD_56_css_iframe = ''
OS_FDD_56_xpath = '//*[@id="app"]/section/section/main/div/div[2]/div[4]/div[2]/div[3]/table/tbody/tr[1]/td[7]'
OS_FDD_56_css = '#app > section > section > main > div > div.el-tabs__content > div.box-card > div.el-table.el-table--fit.el-table--border.el-table--scrollable-x.el-table--enable-row-hover.el-table--enable-row-transition.el-table--mini > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(1) > td.el-table_6_column_105 > div > span'
WS_FDD_56_xpath = '//*[@id="app"]/section/section/main/div/div[2]/div[4]/div[2]/div[3]/table/tbody/tr[1]/td[8]'
WS_FDD_56_css = '#app > section > section > main > div > div.el-tabs__content > div.box-card > div.el-table.el-table--fit.el-table--border.el-table--scrollable-x.el-table--enable-row-hover.el-table--enable-row-transition.el-table--mini > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(1) > td.el-table_6_column_106 > div > div > span'

#TDD-55
OS_TDD_55_xpath = '//*[@id="app"]/section/section/main/div/div[2]/div[4]/div[2]/div[3]/table/tbody/tr[2]/td[7]'
OS_TDD_55_css = '#app > section > section > main > div > div.el-tabs__content > div.box-card > div.el-table.el-table--fit.el-table--border.el-table--scrollable-x.el-table--enable-row-hover.el-table--enable-row-transition.el-table--mini > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr.el-table__row.expanded > td.el-table_6_column_105 > div > span'
WS_TDD_55_xpath = '//*[@id="app"]/section/section/main/div/div[2]/div[4]/div[2]/div[3]/table/tbody/tr[2]/td[8]'
WS_TDD_55_css = '#app > section > section > main > div > div.el-tabs__content > div.box-card > div.el-table.el-table--fit.el-table--border.el-table--scrollable-x.el-table--enable-row-hover.el-table--enable-row-transition.el-table--mini > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr.el-table__row.expanded > td.el-table_6_column_106 > div > div > span'

#OnlineStatus
OS_GSM_KB_xpath = '//*[@id="app"]/section/section/main/div/div[2]/div[4]/div[2]/div[3]/table/tbody/tr[4]/td[7]'
OS_GSM_KB_css = '#app > section > section > main > div > div.el-tabs__content > div.box-card > div.el-table.el-table--fit.el-table--border.el-table--scrollable-x.el-table--enable-row-hover.el-table--enable-row-transition.el-table--mini > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(4) > td.el-table_6_column_105 > div > span'
WS_GSM_KB_xpath = '//*[@id="app"]/section/section/main/div/div[2]/div[4]/div[2]/div[3]/table/tbody/tr[4]/td[8]'
WS_GSM_KB_css = '#app > section > section > main > div > div.el-tabs__content > div.box-card > div.el-table.el-table--fit.el-table--border.el-table--scrollable-x.el-table--enable-row-hover.el-table--enable-row-transition.el-table--mini > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(4) > td.el-table_6_column_106 > div > div > span'

# 测试结果
resultReportHeadLine = [
    "设备IP",
    "B40功放开启输出功率",#输出功率
    "B1功放开启输出功率",
    "GSM功放开启输出功率",
    "B40功放关闭输出功率",
    "B1功放关闭输出功率",
    "GSM功放关闭输出功率",
    "B40功放开启",#开启
    "B1功放开启",
    "GSM功放开启",
    "B40功放关闭",#关闭
    "B1功放关闭",
    "GSM功放关闭",
    "核心板1软重启",#软重启
    "核心板2软重启",
    "核心板3软重启",
    "核心板1断电重启",#断电重启
    "核心板2断电重启",
    "核心板3断电重启",
    "主控板重启",
    "测试结果"
]

# 测试过程记录
procRecode = [
    "设备IP",
    "功放关闭时间",
    "功放开启时间",
    "核心板1软重启时间",
    "核心板1软重启建立小区时间",
    "核心板2软重启时间",
    "核心板2软重启建立小区时间",
    "核心板3软重启时间",
    "核心板3软重启建立小区时间",
    "核心板1断电重启时间",
    "核心板1断电重启建立小区时间",
    "核心板2断电重启时间",
    "核心板2断电重启建立小区时间",
    "核心板3断电重启时间",
    "核心板3断电重启建立小区时间",
    "主控板重启时间",
    "主控板上线时间",
    "测试结果"
]

lock = threading.Lock()  # 创建Lock对象
################应用接口上##########################
'''
函数名：MCB_Reboot
功能：
    主控板重启测试；（每次重启的间隔时间为30min）；
    标准：
    A、点击重启主控板后，返回主控重启成功的字段；
    B、5秒后登陆控制台（输入映射的IP），登陆失败；
    C、1min钟后登陆控制台（输入映射的IP），登陆成功，能查询到主控版本信息；
    上述三点均满足，则判断此次主控板重启成功；
参数：
    url:地址
返回值：
    ['重启时间','建立小区时间',结果']
修改时间：
    2020年4月29日13:40:15
    2020年4月30日14:03:02
        修改点击重启后延时时间为10s,原本5s时间过短
'''
def MCB_Reboot(url):
    printf("打开浏览器，登录")
    statusVal = 0
    mcbRetStatus = ['','','false']
    driver = login(url)
    mcbRetStatus[0] = time.ctime()
    try:
        driver.find_element_by_xpath(reboot_mcband).click()
        time.sleep(3)
        driver.find_element_by_xpath(comfirm).click()
        time.sleep(3)
        printf("关闭浏览器")
        driver.quit()
        printf('等待10s，登录控制台：预计结果为登录失败')
        time.sleep(10)
        loginStatus = login_test(url)
        if loginStatus == 0:
            printf("重启主控失败")
            statusVal -= 1
            driver.quit()
        else:
            print("重启主控成功")
            statusVal += 1
            driver.quit()
        print("等待一分钟后登录控制台，预计结果为登录成功")
        time.sleep(60)
        loginStatus = login_test(url)
        mcbRetStatus[1] = time.ctime()
        if loginStatus == 0:
            print("重启主控成功")
            statusVal += 2
        else:
            printf("重启主控失败")
            statusVal -= 2
        printf("退出浏览器，等待五分钟后执行功放开关测试")
    except Exception as err:
        printf(err)
        printf("无法连接，请检查设备的是否开启，或是否在同一网段")
    driver.quit()
    if statusVal == 3:
        mcbRetStatus[2] = 'pass'
    else:
        mcbRetStatus[2] = 'false'
    return mcbRetStatus

'''
函数名：PA_Reboot
功能：
    打开功放，记录时间，查询功放输出功率
    关闭功放，记录时间，查询功放输出功率
流程：
    1，初始化参数
    1.2 登录
    2，设置输出功率
    3，关闭所有功放
    4，查询输出功率
    5，开启功放
    6，查询输出功率
    7，返回
err:
    1,打开url失败
    2，定位元素失败
参数：
    url:地址，如http://192.168.3.200/#/login
返回值：
    paRetStatus = [ '时间','false','false','false',
                    '时间','false','false','false']
修改时间：
    2020年4月29日09:59:53
    2020年4月30日14:04:37
        不通过功放输出功率判断开关结果，只需记录功放值 --ok--ok
        通过按钮状态判断是否开关--
        增加刷新后的延迟时间，5s --ok
        返回值添加功放值列 --ok
'''
def PA_Reboot(url):
    paRetStatus = ['','false','false','false',
                   '','false','false','false']
    paCheckValus = ['-999'] * 6
    indexNu = 0
    driver = login(url)
    try:
        time.sleep(1)
        driver.find_element_by_xpath(jz_manage).click()  # 点击基站管理
        time.sleep(1)

        #set_output_40dbm(driver)
        printf("点击功放管理")
        driver.find_element_by_xpath(pa_manage).click()
        time.sleep(1)

        closePaStr = time.ctime()#记录关闭功放时间
        paRetStatus[indexNu] = closePaStr
        indexNu += 1

        driver.find_element_by_xpath(pa_off).click()
        printf("关闭所有功放：" + time.ctime())
        time.sleep(5)

        driver.find_element_by_xpath(refresh).click()
        printf("点击刷新")
        time.sleep(3)

        # 读取表内容，循环获取三个功放值
        strIn = [ "NULL"]*4
        strStatusIn = ['NULL']*4
        cssStrPa1 = 'main > div > div.el-tabs__content > div.box-card > div.el-table.el-table--fit.el-table--border.el-table--scrollable-x.el-table--enable-row-hover.el-table--enable-row-transition.el-table--mini > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(1) > td.el-table_1_column_9 > div > div > span'
        cssStrPa2 = 'main > div > div.el-tabs__content > div.box-card > div.el-table.el-table--fit.el-table--border.el-table--scrollable-x.el-table--enable-row-hover.el-table--enable-row-transition.el-table--mini > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(2) > td.el-table_1_column_9 > div > div > span'
        cssStrPa3 = 'main > div > div.el-tabs__content > div.box-card > div.el-table.el-table--fit.el-table--border.el-table--scrollable-x.el-table--enable-row-hover.el-table--enable-row-transition.el-table--mini > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(3) > td.el-table_1_column_9 > div > div > span'
        cssClosePaStatus1 = 'main > div > div.el-tabs__content > div.box-card > div.el-table.el-table--fit.el-table--border.el-table--scrollable-x.el-table--enable-row-hover.el-table--enable-row-transition.el-table--mini > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(1) > td.el-table_1_column_12 > div > div > span'
        cssClosePaStatus2 = 'main > div > div.el-tabs__content > div.box-card > div.el-table.el-table--fit.el-table--border.el-table--scrollable-x.el-table--enable-row-hover.el-table--enable-row-transition.el-table--mini > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(2) > td.el-table_1_column_12 > div > div > span'
        cssClosePaStatus3 = 'main > div > div.el-tabs__content > div.box-card > div.el-table.el-table--fit.el-table--border.el-table--scrollable-x.el-table--enable-row-hover.el-table--enable-row-transition.el-table--mini > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr:nth-child(3) > td.el-table_1_column_12 > div > div > span'
        strIn[1] = cssStrPa1
        strIn[2] = cssStrPa2
        strIn[3] = cssStrPa3
        strStatusIn[1] = cssClosePaStatus1
        strStatusIn[2] = cssClosePaStatus2
        strStatusIn[3] = cssClosePaStatus3
        for i in {1,2,3}:
            try:
                driver, ret_val = get_pa_val(driver, strIn[i]) #获取功放值
                paCheckValus[i-1] = ret_val
                get_pa_property(driver, strStatusIn[i])
            except Exception as err:
                printf(err)
                printf(sys._getframe().f_lineno)
                continue


        # 点击开启功放,3秒后，点击刷新，读取功放输出功率为（38-40）dbm
        openPaStr = time.ctime() #记录功放开启时间
        paRetStatus[indexNu] = openPaStr
        indexNu += 1
        driver.find_element_by_xpath(pa_on).click()
        printf("开启所有功放")
        time.sleep(5)
        driver.find_element_by_xpath(refresh).click()
        printf("点击刷新")
        time.sleep(3)
        for i in {1, 2, 3}: #循环获取三个功放值
            try:
                driver, ret_val = get_pa_val(driver, strIn[i]) #获取功放值
                paCheckValus[i-1+3] = ret_val
                get_pa_property(driver,strStatusIn[i])
            except Exception as err:
                printf(err)
                printf(sys._getframe().f_lineno)
                continue
    except Exception as err:
        #进入这里的一般是登录出错，网页无法打开，设备无法连接的原因
        printf(err)
        printf(sys._getframe().f_lineno)
        printf("无法连接，请检查设备的是否开启，或是否在同一网段")
        paRetStatus[0] = time.ctime()
        paRetStatus[1] = 'false'
    driver.quit()
    return paRetStatus,paCheckValus

'''
函数名：KB_Reboot
功能：
    核心板软重启，核心板断电重启
流程：
    初始化参数
    登录
    击基站管理 jz_manage
    点击核心板管理
    点击第band_n块板
    点击rebootType重启
    点击重启确认按钮
    
入参：
    url:地址
    rebootType：重启类型
    band_n：选择第几块板
返回值：['重启时间','建立小区时间'结果']
修改时间：2020年4月29日13:43:23
'''
def KB_Reboot(url,rebootType,band_n):
    kbRetStatus = -1
    kbStatus = ['', '', 'false']
    main_xpath = '//*[@id="app"]/section/section/main'
    fresh_click = 'main > div > div.el-tabs__content > div.box-card > div.search.el-row > div > button > span'
    first_css = 'main > div > div.el-tabs__content > div.box-card > div.el-table.el-table--fit.el-table--border.el-table--scrollable-x.el-table--enable-row-hover.el-table--enable-row-transition.el-table--mini > div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr.el-table__row.expanded > td.el-table_1_column_7 > div > span'

    driver = login(url)
    kbStatus[0] = time.ctime()
    try:
        time.sleep(1)
        driver.find_element_by_xpath(jz_manage).click()
        printf("点击基站管理")
        time.sleep(1)

        driver.find_element_by_xpath(band_manage).click()
        printf("点击核心板管理")
        time.sleep(1)

        click_band_n(driver,band_n)
        printf("点击第band_n块板:")
        printf(band_n)
        time.sleep(1)

        driver.find_element_by_xpath(rebootType).click()
        printf("点击rebootType重启：")
        printf(rebootType)
        time.sleep(1)

        driver.find_element_by_xpath(comfirm_soft).click()
        printf("点击重启确认")
        time.sleep(1)
        for i in {1, 2, 3, 4}:
            if i == 1:
                printf("等待5s")
                time.sleep(5)
            elif i == 2:
                printf("等待20s")
                time.sleep(20)
            elif i == 3:
                printf("等待60s")
                time.sleep(60)
            elif i == 4:
                printf("等待180s")
                time.sleep(3 * 60)

            time.sleep(1)
            locater = driver.find_element_by_xpath(main_xpath)
            time.sleep(1)
            locater.find_element_by_css_selector(fresh_click).click()
            printf("点击刷新")
            time.sleep(1)
            retStr = locater.find_element_by_css_selector(first_css).text
            printf("基带板工作状态查询：")
            printf(retStr)
            if "离线" in retStr:
                printf("离线状态")
            elif "在线" in retStr:
                printf("在线状态")
                kbRetStatus += 1
                kbStatus[1] = time.ctime()
            else:
                printf("非离线-在线状态：")
        time.sleep(1)
        printf("关闭浏览器")
        driver.quit()
    except Exception as err:
        printf(err)
        printf(sys._getframe().f_lineno)
        printf("无法连接，请检查设备的是否开启，或是否在同一网段")

    if kbRetStatus >= 0:  #重启成功
        kbStatus[2] = "pass"
    else:
        kbStatus[2] = "false"
    return kbStatus

################应用接口下##########################

################底层接口上##########################

#创建新excel文件
'''
函数名：openpyxl_create_report
功能：创建新excel文件
入参：
    fileName：文件名
    tableNames：表名，数组
返回值：无
修改时间：2020年4月29日14:54:30
'''
def openpyxl_create_report(fileName,tableNames):
    path = '../report/' + fileName + ".xlsx"
    data = openpyxl.Workbook() # 新建工作簿
    i = 0
    for name in tableNames:
        data.create_sheet(name, i)  # 添加页,设置第一个工作页
        i += 1
    data.save(path) # 一定要保存

'''
函数名：openpyxl_addin
功能：
    向excel追加内容
    设置字体表格颜色
    设置居中对齐
入参：
    fileName：文件名
    tableName：表名
    values：写入数组
    IfHead：是否为第一行（0）
返回值：
修改时间：
'''
def openpyxl_addin(fileName,tableName,values,IfHead):
    fileName = '../report/' + fileName + ".xlsx"
    data = openpyxl.load_workbook(fileName)
    table = data.get_sheet_by_name(tableName)
    nrows = table.max_row  # 获得行数+1的值，即下一行应该写入的地方
    if IfHead == 0:
        pass #此时为标题头
    else:
        nrows += 1
    col = 1
    resultFlags = 0
    for value in values:
        print("value:%s,row:%d,col:%d"%(value,nrows,col))
        table.cell(row=nrows, column=col).value = value
        if 'pass' in value:
            #设置字体颜色
            table.cell(row=nrows, column=col).fill = green_fill
        elif 'false' in value:
            resultFlags += 1
            table.cell(row=nrows, column=col).fill = red_fill
        #设置居中对齐
        table.cell(row=nrows, column=col).alignment = Alignment(horizontal='center', vertical='center')
        col += 1
    data.save(fileName)

'''
函数名：printf
功能：打印日志，控制台输出
参数：输出文本
返回值：无
修改时间：2020年4月29日14:39:44
'''
def printf(test):
    logger.info("[%d]%s" % (threading.currentThread().ident,test))

'''
函数名：login_test
功能：
    登录
入参：
    url:地址
返回值：
    0：登录成功
    -1:登录失败
修改时间：2020年4月29日14:38:01
'''
def login_test(url):
    printf("打开浏览器")
    driver = webdriver.Chrome(Chrome_path)
    driver.implicitly_wait(30)
    try:
        driver.get(url)
        driver.maximize_window()
        printf("开始登录操作")
        driver.find_element_by_xpath(inputuser_box).send_keys("admin")
        driver.find_element_by_xpath(inputpasswd_box).send_keys("GDJC6880")
        driver.find_element_by_xpath(login_submit_btn).click()
        printf("点击了登录按钮")
    except:
        printf("登录异常,关闭浏览器")
        driver.quit()
        printf(sys._getframe().f_lineno)
        return -1
    else:
        printf("登录成功")
        return 0

'''
函数名：login
功能：
    登录
入参：
    url:地址
返回值：
    driver：登录页面句柄
修改时间：2020年4月29日14:38:01
'''
def login(url):
    printf("打开浏览器")
    driver = webdriver.Chrome(Chrome_path)
    driver.implicitly_wait(30)
    try:
        driver.get(url)
        driver.maximize_window()
        printf("输入用户名："+"admin")
        driver.find_element_by_xpath(inputuser_box).send_keys("admin")
        printf("输入密码："+"GDJC6880")
        driver.find_element_by_xpath(inputpasswd_box).send_keys("GDJC6880")
        driver.find_element_by_xpath(login_submit_btn).click()
        printf("点击了登录按钮")
        return driver
    except Exception as err:
        printf(err)
        printf(sys._getframe().f_lineno)
        driver.quit()
        return driver

'''
函数名：set_output_40dbm
功能:设置核心板输出功率为40dbm
返回值:无
修改时间：2020年4月29日14:42:25
'''
def set_output_40dbm(driver):
        #点击核心板管理
        driver.find_element_by_xpath(band_manage).click()
        #time.sleep(1)
        # 点击第一块板子
        click_band_1(driver)
        # 点击参数设置
        click_setpar_band(driver)
        # 设置输出功率为40dbm
        type_UePMax(driver,"40")
        time.sleep(1)
        # 保存
        click_save_par(driver)
        time.sleep(1)
        click_save_par_confirm(driver)
        time.sleep(1)

'''
函数名：get_pa_val
功能：读取功放值
入参：
    driver:页面句柄
    cssStr：css元素定位
返回值：
    driver：页面句柄
    ret_val：功放输出功率值
修改时间：2020年4月29日14:45:15
'''
def get_pa_val(driver,cssStr):
    ret_val = -999
    try:
        main_xpath = '//main[@class="el-main main"]'
        locater = driver.find_element_by_xpath(main_xpath)
        ret_val = locater.find_element_by_css_selector(cssStr).text
        printf(ret_val)
    except Exception as err:
        printf(err)
    return driver, ret_val

'''
函数名：get_pa_property
功能：读取按钮属性值
入参：
    driver:页面句柄
    cssStr：css元素定位
返回值：
    driver：页面句柄
    ret_val：功放输出功率值
修改时间：2020年4月29日14:45:15
'''
def get_pa_property(driver,cssStr):
    ret_val = ''
    try:
        main_xpath = '//main[@class="el-main main"]'
        locater = driver.find_element_by_xpath(main_xpath)
        pa_status = locater.find_element_by_css_selector(cssStr)
        ret_val = pa_status.value_of_css_property('style')
        printf(ret_val)
    except Exception as err:
        printf(err)
    return driver, ret_val

# 点击第一块基带板
def click_band_1(driver):
    printf("点击第一块基带板")
    driver.find_element_by_xpath(band_1).click()
    time.sleep(1)

'''
函数名：click_band_n
功能：点击第band_n块包板
入参：
    driver：句柄
    band_n：第n块板xpath
返回值：
修改时间：2020年4月29日14:47:05
'''
def click_band_n(driver,band_n):
    printf(band_n)
    driver.find_element_by_xpath(band_n).click()
    time.sleep(1)

#点击参数设置
def click_setpar_band(driver):
    #self.clicks(self.setpar_band)
    printf("点击参数设置")
    driver.find_element_by_xpath(driver.setpar_band).click()
    time.sleep(1)

#清空并输入输出功率(dBm) clear() send_keys
def type_UePMax(driver,text):
    printf("清空并输入输出功率")
    driver.find_element_by_xpath(UePMax).clear()
    driver.find_element_by_xpath(UePMax).send_keys(text)

#保存参数
def click_save_par(driver):
    printf("保存参数")
    driver.find_element_by_xpath(save_par).click()

# 保存参数成功，点击确定按钮
def click_save_par_confirm(driver):
    printf("点击确定按钮")
    driver.find_element_by_xpath(comfirm_button).click()
##############底层接口下############################

###############测试用例#################################
'''
函数名：App
功能： 
   功放开关
   核心板软启动
   核心板断电重启
   主控重启
   测试结果输出报告
参数：
    ip:设备ip
    nu：入参延时
修改时间：
    2020年4月29日10:43:01
    2020年4月30日14:12:59
        结果记录长度增加到22：原本为values = [''] * 16
        功放无法通过包含值来判断是否为记录结果
'''
def App(ip,nu):
    global lock  # 声明为全局变量,每个线程函数中都要声明
    time.sleep(nu)
    Rep_Num = 0
    Proc_Num = 0
    values = [''] * 22
    valuesProcTime = [''] * 32
    values[Rep_Num] = ip
    Rep_Num += 1
    valuesProcTime[Proc_Num] = ip
    Proc_Num += 1

    url ="http://"+ ip +"/#/login"
    for i in range(30):
        Rep_Num = 1
        Proc_Num = 1
        printf(url)
        printf("开始功放开关测试")

        paRetArr,paCheckValus = PA_Reboot(url)
        print("paCheckValus return :%s" % paCheckValus)
        for paValue in paCheckValus:
            values[Rep_Num] = paValue
            Rep_Num += 1

        print("Pa_reboot return :%s" % paRetArr)
        for paValue in paRetArr:
            if 'false' in paValue or 'pass' in paValue:
                values[Rep_Num] = paValue
                Rep_Num += 1
            else:
                valuesProcTime[Proc_Num] = paValue
                Proc_Num += 1

        printf("等待4分钟")
        time.sleep(4 * 60)
        band_n = ''
        for n in {1,2,3}:
            if n == 1:
                band_n = band_1
            elif n == 2:
                band_n = band_2
            elif n == 3:
                band_n = band_3

            printf("第%d块板软重启" % n)
            kbRetArr = KB_Reboot(url, reboot_band, band_n)
            for kbValue in kbRetArr:
                if 'false' in kbValue or 'pass' in kbValue:
                    values[Rep_Num] = kbValue
                    Rep_Num += 1
                else:
                    valuesProcTime[Proc_Num] = kbValue
                    Proc_Num += 1

        ###断电重启
        printf("等待4分钟")
        time.sleep(4 * 60)
        printf("开始断电重启测试")
        for n in {1, 2, 3}:
            if n == 1:
                band_n = band_1
            elif n == 2:
                band_n = band_2
            elif n == 3:
                band_n = band_3
            printf("第%dd块板断电重启" % n)
            kbRetArr = KB_Reboot(url, power_outage_restart, band_n)
            for kbValue in kbRetArr:
                if 'false' in kbValue or 'pass' in kbValue:
                    values[Rep_Num] = kbValue
                    Rep_Num += 1
                else:
                    valuesProcTime[Proc_Num] = kbValue
                    Proc_Num += 1
        ###主控重启
        printf("等待4分钟")
        time.sleep(4 * 60)
        printf("主控重启测试")
        mcbRetArr = MCB_Reboot(url)
        for mcbValue in mcbRetArr:
            if 'false' in mcbValue or 'pass' in mcbValue:
                values[Rep_Num] = mcbValue
                Rep_Num += 1
            else:
                valuesProcTime[Proc_Num] = mcbValue
                Proc_Num += 1

        #加锁
        lock.acquire()  # 上锁，之后的同步代码，只能一个线程访问
        #修改格式，先把所以的需要的时间和结果记录，然后在写之前区分
        openpyxl_addin(filename, "测试结果", values, 1)
        openpyxl_addin(filename, "测试过程记录", valuesProcTime, 1)
        lock.release()  # 解锁
        #解锁
        printf("等待14分钟")
        time.sleep(14 * 60)

    print("END")

def TTT_Index():
    pass

if __name__=='__main__':
    '''
    
    tableNames = ["测试结果", "测试过程记录"]
    openpyxl_create_report(filename, tableNames)
    openpyxl_addin(filename, "测试结果", resultReportHeadLine, 0)
    openpyxl_addin(filename, "测试过程记录", procRecode, 0)
    threads = []
    IP = ("192.168.3.200",
          "192.168.3.201",
          "192.168.3.202",
          "192.168.3.203"
          )
    nu = 1
    for i in {0,1,2,3}:
        str = "创建线程" + IP[i]
        printf(str)
        thd1 = threading.Thread(target=App, args=(IP[i], nu))  # 创建一个线程
        nu += 5
        threads.append(thd1)

    for th in threads:
        th.start()  # start()---启动线程活动 GDJC6880
        time.sleep(5)
    for th in threads:
        th.join()  # 等待线程结束
    '''
    #retVal = PA_Reboot("http://192.168.3.200/#/login")
    #retVal = KB_Reboot(url, reboot_band, band_1)
    #printf(retVal)

    login('http://192.168.3.200/#/login')
    ret = KB_Reboot('http://192.168.3.200/#/login', power_outage_restart, band_2)

