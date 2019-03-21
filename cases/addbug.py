from selenium import webdriver
from common.base import Base
from cases.loginpage import ZenTaoLogin

class AddBugPage(Base):
    loc_test = ("link text", "测试")
    loc_bug = ("link text", "Bug")
    loc_tijiao = ("xpath", ".//*[@id='createActionMenu']/a")
    loc_module = ("xpath", ".//*[@id='module_chosen']/a")
    loc_login = ("xpath", ".//*[@id='module_chosen']/div/ul/li[1]")
    loc_banben = ("xpath", ".//*[@id='openedBuild_chosen']/ul")
    loc_truk = ("xpath", ".//*[@id='openedBuild_chosen']/div/ul/li[1]")
    loc_title = ("id", "title")

    # 正文切换iframe
    frame = ("class name", "ke-edit-iframe")
    loc_body = ("class name", "article-content")
    # 切回主页
    loc_save = ("id", "submit")

    # 判断元素
    loc_result = ("xpath", ".//*[@id='bugList']/tbody/tr[1]/td[4]/a")

    def add_bug(self, title="测试title_01", body="正文"):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_tijiao)
        self.click(self.loc_module)
        self.click(self.loc_login)
        self.click(self.loc_banben)
        self.click(self.loc_truk)
        self.send(self.loc_title, title)
        # 切换iframe
        f = self.find(self.frame)  # element对象
        self.driver.switch_to.frame(f)
        self.send(self.loc_body, body)
        # 切回
        self.driver.switch_to.default_content()
        self.click(self.loc_save)

    def get_title_result(self, _text):
        '''返回布尔值, _text是期望文本值'''
        r = self.text_in_element(self.loc_result, _text)
        return r

if __name__ == '__main__':
    # 封装完成后先调试
    driver = webdriver.Firefox()
    driver.get("http://47.104.190.48:8088/zentao/user-login-L3plbnRhby8=.html")
    zen = ZenTaoLogin(driver)
    zen.login()  # 登录流程
    # 提交BUG流程
    bug = AddBugPage(driver)
    bug.add_bug(title="测试22222")   # 提交BUG流程




