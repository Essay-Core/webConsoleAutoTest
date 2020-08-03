#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import configparser
import os.path
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):
    """
    定义一个浏览器引擎类，根据browser_type的值去控制不同的浏览器
    """

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path, encoding='UTF-8')

        browser = config.get("browserType", "browserName")
        logger.info("本次测试使用浏览器：Chrome")
        url = config.get("testServer", "URL")
        # logger.info("本次测试连接url:http://192.168.3.248")

        if browser == 'Firefox':
            driver = webdriver.Firefox()
            logger.info("Firefox已经启动...")

        elif browser == 'Chrome':
            #option = webdriver.ChromeOptions()
            #option.add_argument('disable-infobars')

            #driver = webdriver.Chrome(chrome_options=option)
            Chrome_path = r"D:\code_2018_1031\consoleTest\consoleTest\\tools\chromedriver.exe"
            driver = webdriver.Chrome(Chrome_path)
            logger.info("Chrome已经启动...")

        elif browser == 'IE':
            driver = webdriver.Ie()
            logger.info("Ie已经启动...")

        else:
            option = webdriver.ChromeOptions()
            option.add_argument('disable-infobars')
            driver = webdriver.Chrome(chrome_options=option)
            logger.info("Chrome已经启动...")

        driver.get(url)
        # logger.info("打开连接：http://192.168.3.200")
        driver.maximize_window()
        logger.info("浏览器窗口最大化")
        driver.implicitly_wait(10)
        return driver

    def quit_browser(self):
        logger.info("测试执行完毕，退出并关闭浏览器")
        self.driver.quit()

