import unittest
import time
def add(a, b):
    '''两个数相加'''
    c = a+b
    return c

class TestAdd(unittest.TestCase):

    # 类方法
    @classmethod
    def setUpClass(cls):
        print("用例之前只执行一次")

    @classmethod
    def tearDownClass(cls):
        print("用例最后只执行一次")


    def setUp(self):
        '''前置操作'''
        time.sleep(1)
        print("打开浏览器")       # 所有用例之前都会执行一次

    def tearDown(self):
        '''数据清理，后置操作'''
        time.sleep(1)
        print("关闭浏览器")        # 所有用例之后都会执行一次

    def test_add(self):
        '''测试数据： 2  ， 4'''
        time.sleep(1)
        print("第一个测试用例")
        r = add(2, 4)  # 实际结果
        exp = 6
        self.assertEqual(r, exp)
    def test_add2(self):
        '''测试数据： "hello"  ， "world"'''
        time.sleep(1)
        print("第二个测试用例")
        r = add("hello", "world")
        exp = "helloworld"
        self.assertEqual(r, exp)

if __name__ == "__main__":
    unittest.main()