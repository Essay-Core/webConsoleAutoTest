#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.console_homepage import HomePage

class consoleLogin(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_console_login_pass(self):
        login = HomePage(self.driver)
        login.type_user("admin")
        login.type_pwd("GDJC6880")
        login.send_login_btn()
        time.sleep(3)
        try:
            login.get_windows_img()  # 调用基类截图方法
            t = self.driver.find_element_by_xpath("//div[text()='首页']").text
            assert '首页' in t
            print("pass")
        except Exception as e:
            print("fail",format(e))

    def test_console_login_false(self):
        login = HomePage(self.driver)
        UserPasswd = (['111', '222'],
                      ["admin", ""],
                      ["用户名admin", ""],  # 3
                      ["averylongadminname12345678901234567890", ""],
                      ["", "123456"],  # 账户名为空
                      ["", "123456密码"],
                      ["", "123 456"],
                      ["", "12345"],
                      ["", "654321"],
                      ["", "654321"],  # 密码格式错误
                      ["Notadmin", "中文654321"],
                      ["Notadmin", "654 321"],
                      ["Notadmin", "65431"],
                      ["Notadmin", "12345678901234567890"],
                      ["admin", "中文654321"],
                      ["admin", "654 321"],
                      ["admin", "65431"],
                      ["admin", "12345678901234567890"],
                      ["中文admin", "654321"],  # 输入格式错误的用户名 21
                      ["admin￥&", "654321"],
                      ["admin12345678901234567890", "654321"],
                      ["中文admin", "123456"],
                      ["admin%$", "123456"],
                      ["中文%￥#admin123456789012345678901234567890", "123456"],  # 26
                      ["admin123456789012345678901234567890", "中文%￥#123456"]  # 27
                      )
        for i in range(len(UserPasswd)):
            print('账号 :%s, 密码：%s' % (UserPasswd[i][0], UserPasswd[i][1]))
            login.type_user(UserPasswd[i][0])
            login.type_pwd(UserPasswd[i][1])
            login.send_login_btn()
            time.sleep(3)
            try:
                # 测试条件：没有成功，停留在登录界面，判断还有成功按钮即表示成功
                # 根据执行的结果页面的元素进行定位
                t = self.driver.find_element_by_xpath("//span[text()='登录']").text
                assert '登录' in t
                print("pass")
            except Exception as e:
                print("fail", format(e))
                return

if __name__=='__main__':
    unittest.main()