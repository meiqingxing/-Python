"""

"""
import matplotlib.pyplot as plt

# # 绘制一个点
# plt.scatter(2, 4, s=200)  # s指定点的尺寸

# # 绘制一系列的点
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.scatter(x_values, y_values, s=100)

# 绘制1000个点
x_values = list(range(1, 1001))
y_values = [a**2 for a in x_values]
# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=5)  # 点内部颜色为red，外部轮廓none
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=5)  # RGB颜色模式：值越接近0，指定的颜色越深；值越接近1，指定的颜色越浅
# 颜色映射
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=1)  # 将参数c设置为y值列表，并用参数cmap告诉pyplot使用哪一个颜色映射

# 设置图标标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置每个坐标值的取值范围
plt.axis([0, 1100, 0, 1100000])  # (x坐标最小和最大值，y坐标最小和最大值)

# plt.show()
# 上一行替换为plot.savefig()的调用：将图表自动保存到文件中
plt.savefig('squares_pot.png', bbox_inches='tight')  # (文件名，指定将图表多余的空白区域裁减掉)
