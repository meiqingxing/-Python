"""
掷骰子
"""
from random import randint
import pygal

class Die():
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):  # 如果没有指定任何实参，面数默认6
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机值"""
        return randint(1, self.num_sides)


# # 创建一个D6
# die = Die()

# # 创建两个D6骰子
# die_1 = Die()
# die_2 = Die()

# 创建一个D6和一个D10
die_1 = Die()
die_2 = Die(10)

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()  # 将每次掷时的两个骰子的点数相加，并存储在result中
    results.append(result)
print(results)

# 分析结果；计算每个点出现的次数
frequencies = []
# for value in range(2, 13):
max_result = die_1.num_sides + die_2.num_sides  # 可能出现的最大点数为两个骰子的最大可能点数：12
for value in range(2, max_result+1):
    frequency = results.count(value)  # 统计点value出现的次数
    frequencies.append(frequency)

print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 1000 times"  # 标示直方图的字符串
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']  # x轴标签
hist.x_title = "Result"  # x轴标题
hist.y_title = "Frequency of Result"  # y轴标题

hist.add("D6 + D10", frequencies)  # 传递要给添加的值指定的标签，还有一个列表（其中包含将出现在图表中的值）
hist.render_to_file('dice_visual.svg')