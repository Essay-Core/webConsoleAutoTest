#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os
import time
from selenium.common.exceptions import NoSuchAttributeException
from framework.logger import Logger

logger = Logger(logger='BasePage').getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("浏览器后退")

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("浏览器前进")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("等待 %d 秒" %seconds)

    # 关闭并停止浏览器服务
    def quit_browser(self):
        self.driver.quit()
        logger.info("关闭浏览器")

    # 保存图片
    def get_windows_img(self):
        """
        截图并保存在根目录下的Screenshot文件夹下
        """
        file_path = os.path.dirname(os.getcwd()) + '/Screenshots/'
        rq = time.strftime('%Y%m%d%H%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("开始截图并保存")
        except Exception as e:
            logger.error("测试截图失败！%s" % e)
            self.get_windows_img()

    # 定位元素方法
    def find_element(self, selector):
        """
        使用=>来切割字符串
        :param selector:
        :return:
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("通过 %s via value: %s 定位元素成功：\'%s\' " % (selector_by, selector_value, element.text))
            except NoSuchAttributeException as e:
                logger.error("NoSuchAttributeException: %s" % e)
                self.get_windows_img()
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("通过 %s via value: %s 定位元素成功：\'%s\' " % (selector_by, selector_value, element.text))
            except NoSuchAttributeException as e:
                logger.error("NoSuchAttributeException: %s" % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("please enter a valid type of targeting elements.")
        return element

    # 输入
    def inputText(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("输入文本内容：\' %s '" % text)
        except NameError as e:
            logger.error("输入文本内容失败：%s" % e)
            self.get_windows_img()

    # 清除文本框
    def clearText(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("清除输入文本.")
        except NameError as e:
            logger.error("清除文本: %s ，失败" % e)
            self.get_windows_img()

    # 点击元素
    def clicks(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("元素\'%s'\ 被点击." % el.text)
        except NameError as e:
            logger.error("点击元素失败：%s" % e)

    #获取元素文本
    def get_eText(self, selector):
        el = self.find_element(selector).text
        return el

    # 获取网页标题
    def get_page_title(self):
        logger.info("当前页面的网页标题是：%s" % self.driver.title)
        return self.driver.title

    # 休眠时间
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)
