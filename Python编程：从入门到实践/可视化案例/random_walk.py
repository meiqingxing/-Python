"""
模拟随机漫步，创建一个名为RandomWalk的类：需要三个属性
其中一个存储随机漫步次数的变量，其他两个是列表，村粗随机漫步经过的点的x和y坐标

"""
from random import choice

class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):  # 计算随机漫步经过的所有点
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机漫步都始于（0， 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点，并决定每次慢步的方向"""

        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])  # 向哪走？ 要么是想左走的-1，要么是向右走的1
            x_distance = choice([0, 1, 2, 3, 4])  # 走多远？
            x_step = x_direction * x_distance  # 沿x轴的距离

            y_direction = choice([1, -1])
            y_distance = choice(range(0, 5))
            y_step = y_direction * y_distance  # 沿y轴的距离

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue  # 如果原地踏步，接着执行下一次循环

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step  # 获得漫步中下一个点的值
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)  # 将获得的x y值添加到列表里
            self.y_values.append(next_y)



import matplotlib.pyplot as plt

# 只要程序处于活动状态，就不断的模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(10000)  # 更改点数
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6))  # 用于指定图表的宽度、高度，分辨率和背景色；指定元组，单位为英寸

    # 设置一个列表，其中包含个点的先后顺序，根据漫步中各个点的先后顺序进行着色
    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=5)
    # 将随机漫步包含的x和y值传递给scatter()，利用参数c指定使用颜色映射Blues，传递实参edgecolors删除每个点周围的轮廓，并选择了合适的点尺寸

    # 突出起点和终点；让起点和终点更大且颜色不一样
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)  # 起点
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)  # 终点

    # 隐藏坐标轴
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

"""
这些随机漫步都在起点附近进行，大多沿特定方向偏离起点，漫步点分布不均匀。
"""