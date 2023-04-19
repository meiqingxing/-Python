import matplotlib.pyplot as plt

"""多合一显示"""
import numpy

# fig = plt.figure()
#
# plt.subplot(2, 1, 1)  # 将整个figure分成两行、两列； 1：第一张图，占三个图的位置
# plt.plot([0, 1], [0, 1], )
#
# plt.subplot(2, 3, 4)  # 第2张图，从4开始
# plt.plot([0, 1], [0, 2], )
#
# plt.subplot(2, 3, 5)  # 第3张图
# plt.plot([0, 1], [0, 3], )
#
# plt.subplot(236)  # 第4张图；可以省略逗号
# plt.plot([0, 1], [0, 4], )
#
# plt.show()


"""分格显示"""
# method1: subplot2frid
# ####################################
# import matplotlib.gridspec as gridspec

# plt.figure()
# ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)
# # (3, 3):3行,3列；(0,0):从第1行第1列开始；col=3:占3列；row=1:占1行
# ax1.plot([1, 2], [1, 2])
# ax1.set_xlabel('x')
# ax1.set_title('ax1_title')
# ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=1)
# ax3 = plt.subplot2grid((3, 3), (1, 2), colspan=1, rowspan=2)
# ax4 = plt.subplot2grid((3, 3), (2, 0), colspan=1, rowspan=1)
# ax5 = plt.subplot2grid((3, 3), (2, 1), colspan=1, rowspan=1)

# method2: gridspec
# ####################################
# import matplotlib.gridspec as gridspec
# plt.figure()
# gs = gridspec.GridSpec(3, 3)
# ax6 = plt.subplot(gs[0, :])  # 占第1行，所有列
# ax7 = plt.subplot(gs[1, :2])  # 占第2行，第1、2列
# ax8 = plt.subplot(gs[1:, 2])  # 占第2行之后的（2、3行），第3列
# ax9 = plt.subplot(gs[2, 0])  # 占第3行，第1列
# ax10 = plt.subplot(gs[-1, -2])  # 占倒数第1行，倒数第2列

# method3: easy to define structure
# ####################################
# f, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, sharex=True, sharey=True)  # 共享x、y轴
# ax11.scatter([1, 2], [1, 2])

"""图中图"""
fig = plt.figure()
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 6, 5, 2, 4, 9]

left, bottom, width, height = 0.1, 0.1, 0.8, 0.8  # 相当于整个figure的长度和高度
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x, y, 'red')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

left, bottom, width, height = 0.2, 0.6, 0.20, 0.20
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x, y, 'blue')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title inside 2')

plt.axes([0.6, 0.2, 0.20, 0.20])
plt.plot(x, y[:], 'green')
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 1')


plt.tight_layout()  # 设置子图的间距，默认
plt.show()
