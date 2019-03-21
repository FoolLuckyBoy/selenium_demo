import unittest
from common.HTMLTestRunner import HTMLTestRunner
import os

# 获取当前运行的目录
dirpath = os.path.dirname(os.path.realpath(__file__))  # 文件夹层
print(dirpath)

# 获取用例目录
casespath = os.path.join(dirpath, "cases")
print(casespath)

# 报告目录
reportpath = os.path.join(dirpath, "report", "result.html")
print(reportpath)

reportx = os.path.join(dirpath, "reportx", "result.html")
print(reportx)

# 查找用例的目录
# start_dir = "E:\\project\\cases"  # 地址不要写死
# test*.py 匹配test开头的用例
all = unittest.defaultTestLoader.discover(casespath,
                                    pattern="test*.py")
print(all)

# E:\\project\\report\\result.html"
# 执行用例
fp = open(reportx, "wb")
runner = HTMLTestRunner(stream=fp,
                        title="报告的标题",
                        description="描述测试报告内容。。。",
                        retry=3)
runner.run(all)

# 截图 自动的，selenium代码才可以，必须定义driver(其它参数不可以)

