import unittest
from selenium import webdriver
from cases.qita.read_shujuku import dushujuku

class TestAdd(unittest.TestCase):

    # def tearDown(self):
    #     self.driver.quit()
    #
    # def setUp(self):
    #     self.driver = webdriver.Firefox()
    #     self.driver.get("https://www.baidu.com")
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        # 数据准备
        self.driver.get("https://www.baidu.com")

    def tearDown(self):
        # 数据清理
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_03(self):
        self.driver.find_element_by_id("kw").send_keys("hao")
        # 断言暂时不写
        self.assertTrue(1==2)  # 失败

        # 断言数据库
        r = dushujuku()  # 实际结果
        e = "xxx"
        self.assertTrue(r == e)

    def test_02(self):
        self.driver.find_element_by_id("kw").send_keys("ok")
        # 断言暂时不写

if __name__ == '__main__':
    unittest.main()


