import os

# print(__file__)
# 获取当前运行的xx.py的路径
curpath = os.path.realpath(__file__) # 根据系统获取绝对路径
print(curpath)

dirpath = os.path.dirname(curpath)  # 文件夹层
print(dirpath)

casespath = os.path.join(dirpath, "cases")
print(casespath)

report = os.path.join(dirpath, "report", "result.html")
print(report)

# 没有文件夹的话，会报错

reportx = os.path.join(dirpath, "reportx", "result.html")
print(reportx)


# 判断文件路径是否存在
a = os.path.exists(os.path.join(dirpath, "reporty"))
print(a)

if not a:
    # 创建路径
    os.mkdir(os.path.join(dirpath, "reporty"))

fp = open(reportx, "wb")