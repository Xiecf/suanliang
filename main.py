# coding=utf-8
import math
from fun import *

# 00全隐
# 01横隐竖明
# 10横明竖隐
# 11全明
style = 11  # 00全隐，01横隐竖明，10横明竖隐，11全明
hole_height = 4010  # 洞口高度
hole_width = 4830  # 洞口宽度
fenge = ((750, 1500, 810, 810), (1000, 1150, 1150))  # 窗户中到中分格,(宽，高)
row_width = 60  # 横梁迎面宽度
column_width = 60  # 立柱迎面宽度
standard_size = 6000  # 标准型材长度

print("\n{0}开始计算幕墙用料{0}\n".format("-" * 10))

# 判读窗户尺寸是否超过洞口尺寸
if sum(fenge[0]) + row_width + 30 > hole_width:
    print("注意：窗户宽度超过洞口结构！")
if sum(fenge[1]) + row_width + 30 > hole_height:
    print("注意：窗户高度超过洞口结构！")

# 计算玻璃尺寸
windows = glass(fenge, 11)
print("玻璃:共{}块,尺寸为：\n\t{}".format(len(windows), list_or_dict(windows)))

# 计算立柱???
lizhu = len(fenge[0]) + 1
print("立柱：{}根，长度为{}mm。".format(lizhu, hole_height - 60))
kougai = []
for i in range(len(fenge[0]) + 1):
    kougai.append(sum(fenge[1]) + row_width)
# 计算横梁
print("横梁：")
row = []
for i in range(len(fenge[1]) + 1):
    for j in fenge[0]:
        row.append(j - row_width - 3)
row = caiqie(row)
for i in row:
    for j in i:
        kougai.append(j + 3)
print("扣盖：")
caiqie(kougai)

# 计算埋板、转接件
print("埋板：{}块。".format(lizhu * 2))
print("钢套芯：{}个。".format(lizhu * 2))
print("对穿螺栓：{}套。".format(lizhu * 4))

all_size = fukuang(windows)

# 玻璃下双面胶条
print("双面胶条:{:.0f}米。".format(sum(all_size) / 1000))
# 计算副框用料
print("副框：")
caiqie(fukuang(windows))

# 泡沫棒
foam_stick = sum(fenge[0]) * (len(fenge[1]) + 1) + sum(fenge[1]) * (len(fenge[0]) + 1)
# print("泡沫棒:{:.0f}米".format(foam_stick / 1000))
# print("硅酮密封胶(590ml):{:.0f}支".format(foam_stick / 1000 * 15 * 15 / 590))
print("压板:{}根".format(math.ceil(foam_stick / 400 * 20 / standard_size)))
