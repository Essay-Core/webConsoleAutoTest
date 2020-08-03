#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import unittest
import os
import time
from Lib import HTMLTestReportCN

#设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/report/'

#获取系统当前时间
time = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

#设置报告名称格式
HtmlFile  = report_path + time + "控制台自动化测试报告.html"
fp = open(HtmlFile,"wb")

test_dir = './'
#定义测试目录为当前目录
suite = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ == '__main__':
    #初始化一个HtmlRuner实例对象
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title=u"控制台自动化测试报告",
        description=u"用例测试情况:",
        tester=u"骆炎宽"
    )
    runner.run(suite)
    fp.close()