"""

"""
# 导包
import numpy as np
import matplotlib.pyplot as plt

# 创建一组数据：范围（-3， 3），个数50个
x = np.linspace(-3, 3, 50)

# (x, y1)曲线y1； (x, y2)曲线y2
y1 = 2 * x + 1
y2 = x**2

plt.figure()  # 定义图像窗口
# 图线主体
plt.plot(x, y1, linewidth=1, color='r', linestyle='--')
plt.plot(x, y2, linewidth=1, color='b')

# 定义坐标轴范围
plt.xlim((-5, 5))
plt.ylim((-10, 10))
# 定义坐标轴名称
plt.xlabel('X')
plt.ylabel('Y')

# 定义坐标轴刻度
new_ticks = np.linspace(-5, 5, 5)
plt.xticks(new_ticks)
plt.yticks([-10, -5, 0, 5, 10],
            [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

# 设置图像边框颜色
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 调整刻度位置
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# 调整边框（坐标轴）位置
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# 调整tick的透明度
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(10)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))  # alpha透明度

# 添加图例
l1 = plt.plot(x, y1, label="aaaa")
l2 = plt.plot(x, y2, label="bbbb")
plt.legend(handles=[l1, l2, ], labels=[], loc='best')

# 添加标注
# xycoords坐标基于data；xytext根据offset point这个点+30，-30；arrowprops对箭头进行规定，箭头风格、弧度
x0 = 1
y0 = 2 * x0 + 1
plt.scatter(x0, y0, s=50, color='b')
plt.plot([x0, x0], [y0, 0], 'k--', lw=0.5)
plt.annotate(r'$2x+1=%s$'%y0, xy=(x0, y0), xycoords='data', xytext=(+25, -10), textcoords='offset points',
             fontsize=10, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))

# 添加注释
plt.text(-5, 5, r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$', fontdict={'size': 9, 'color': 'red'})

# 添加标题
plt.title("demo")

# 绘制图形
plt.show()