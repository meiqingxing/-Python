"""

"""
import matplotlib.pyplot as plt

# input_values = [1, 2, 3, 4]
squares = [1, 4, 9, 16, 25]  # 给plot同时提供输入值和输出值

# 线宽
plt.plot(squares, linewidth=5)

# 设置图表标题，并给坐标轴加上标签
plt.title("Squares Numbers", fontsize=24)  # fontsize指定文字大小
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)


plt.show()  # 打开matplotlib查看器，并显示绘制的图形
