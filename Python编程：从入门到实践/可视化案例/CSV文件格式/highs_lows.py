"""
查看文件的第一行
"""

import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取日期、最高温度和最低气温
filename = 'death_valley_2014.csv'  # 待使用的文件名称
with open(filename) as f:

    # reader处理文件中以逗号分隔的第一行数据，并将每项数据都作为一个元素存储在列表中
    reader = csv.reader(f)  # 读取文件对象，创建一个与该文件相关联的阅读器对象（reader）
    header_row = next(reader)  # 将阅读器对象传递给next()时，将返回文件的下一行；调用了一次，所以返回文件的第一行，其中包含文件头

    for index, column_header in enumerate(header_row):  # 对列表调用enumerate()来获取每个元素的索引和值
        print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        """阅读器从停留的地方往下读去CSV文件，每次都自动返回当前所处位置的下一行,由于已经读取了文件头行，所以这个循环将从第二行开始。
           使用try-except-else代码块处理数据缺失；在有些情况下，需要使用continue跳过一些数据，或者remove()或del将提取的数据删除。
        """
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")  # 索引0处（第1列），获取日期
            # 将字符串转换为datetime日期对象
            # 获取最高气温
            high = int(row[1])  # 索引1处（第2列）的数据，获取最高气温
            # 获取最低气温
            low = int(row[3])  # 索引3处（第4列）的数据，获取最低气温

        except ValueError:  # 日期、最高气温、最低气温，只要缺失一项，执行except
            print(current_date, "missing data")  # 打印错误消息

        else:  # 获取的特定日期的所有数据没有发生错误，执行else
            highs.append(high)
            lows.append(low)
            dates.append(current_date)
        # print(highs)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)  # 绘制为红色；alpha指定颜色的透明度，0表示完全透明，1表示完全不透明
plt.plot(dates, lows, c="blue", alpha=0.5)  # 绘制为蓝色
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)  # 指定填充区域，填充区域的颜色，透明度

# 设置图形的格式
title ="Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # 绘制斜的日期标签，以免彼此重叠
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
