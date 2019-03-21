import unittest

def add(a, b):
    '''两个数相加'''
    c = a+b
    return c

class TestAdd(unittest.TestCase):

    def test_add(self):
        '''测试数据： 2  ， 4'''
        r = add(2, 4)  # 实际结果
        exp = 6
        self.assertEqual(r, exp)

    def test_add2(self):
        '''测试数据： "hello"  ， "world"'''
        r = add("hello", "world")
        exp = "helloworld"
        self.assertEqual(r, exp)
        self.assertTrue(1==2)

if __name__ == "__main__":
    unittest.main()