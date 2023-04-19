import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = 0.05 * x**2
y2 = -1 * y1

fig, ax1 = plt.subplots()  # 等价于: fig, ax1 = plt.subplots(1, 1)  # subplots()返回一个figure图像和子图ax的array列表
ax2 = ax1.twinx()  # 将ax2的坐标轴当做ax1反向的坐标轴

ax1.plot(x, y1, 'g-')  # 绿色实线
ax2.plot(x, y2, 'b--')  # 蓝色虚线

ax1.set_xlabel("X data")
ax1.set_ylabel('Y1', color='g')
ax2.set_ylabel('Y2', color='b')

plt.show()