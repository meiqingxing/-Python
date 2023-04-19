import matplotlib.pyplot as plt
import numpy as np


def cal_h(x, y):
    # 算高度的值
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)  # 定义mesh

# 填充颜色
plt.contourf(X, Y, cal_h(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)  # 8：等高线分成10部分（层次）

# 画等高线的线
C = plt.contour(X, Y, cal_h(X, Y), 8, colors='black', linewidths=.5)

# add label
plt.clabel(C, inline=True, fontsize=10)  # True：数字在线里面

plt.xticks(())
plt.yticks(())

plt.show()

