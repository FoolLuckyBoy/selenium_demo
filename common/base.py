from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


class Base():

    def __init__(self, driver:webdriver.Firefox):
        self.driver = driver

    def find(self, locator):
        '''loctor = ("id", "kw")'''
        element = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(*locator))
        return element

    def finds(self, locator):
        '''loctor = ("id", "kw")'''
        elements = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_elements(*locator))
        return elements

    def send(self, locator, _text):
        '''loctor = ("id", "kw")'''
        self.find(locator).send_keys(_text)

    def click(self, locator):
        self.find(locator).click()

    def is_element_exist(self, locator):
        try:
            self.find(locator)
            return True
        except:
            return False

    def text_in_element(self, locator, _text):
        try:
            r = WebDriverWait(self.driver, 30, 1).until(EC.text_to_be_present_in_element(locator, _text))
            return r
        except:
            return False

    def value_in_element(self, locator, _text):
        try:
             r = WebDriverWait(self.driver, 30, 1).until(EC.text_to_be_present_in_element_value(locator, _text))
             return r
        except:
             return False


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://47.104.190.48:8088/zentao/user-login-L3plbnRhby8=.html")

    from selenium.webdriver.common.by import By

    # driver.find_element(By.ID, "id值")
    # driver.find_element("id", "id值")


    b = Base(driver)
    # 登录
    loc1 = ("css selector", "#account")
    b.send(loc1, "admin")

    loc2 = ("css selector", "[name='password']")
    b.send(loc2, "123456")

    loc3 = ("css selector", "#submit")
    b.click(loc3)






