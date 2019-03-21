import time
from selenium import webdriver
import unittest
from common.base import Base

class ZenTaoLogin(Base):

    loc_user = ("css selector", "#account")
    loc_psw = ("css selector", "[name='password']")
    loc_button = ("css selector", "#submit")

    def login(self, user="test123", psw="!@123456"):
        '''登录函数'''
        # 登录
        self.send(self.loc_user, user)
        self.send(self.loc_psw, psw)
        self.click(self.loc_button)

        # self.driver.find_element_by_css_selector("#account").send_keys(user)
        # self.driver.find_element_by_css_selector("[name='password']").send_keys(psw)
        # self.driver.find_element_by_css_selector("#submit").click()

    def get_login_result(self):
        '''获取登录结果'''
        t = ""  # 初始值
        try:
            t = self.driver.find_element_by_css_selector("#userMenu>a").text # 报错
            # print("如果定位到了！")
        except:
            t = ""
        return t

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://47.104.190.48:8088/zentao/user-login-L3plbnRhby8=.html")
    time.sleep(5)

    # 多了一步
    zentao = ZenTaoLogin(driver)
    zentao.login()

    res = zentao.get_login_result()