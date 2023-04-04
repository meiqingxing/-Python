# """
# 扩展列表的sort方法
# 在学习了将函数作为参数传递后，接下来学习列表的sort方法对列表进行自定义排序
# """
# # 准备列表
# my_list = [["a", 33], ["b", 55], ["c", 11]]
# # # 排序，基于带名函数
# # def choose_sort_key(element):
# #     return element[1]
# # my_list.sort(key=choose_sort_key, reverse=True)
# # 排序，基于lambda的匿名函数
# my_list.sort(key=lambda element: element[1], reverse=True)
# print(my_list)

"""
动态柱状图开发
"""
# 导入模块
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
# 读取数据
f = open("E:\Python学习资料\黑马资料\可视化案例数据\动态柱状图数据\全球GDP数据.csv", "r", encoding="GB2312")
data_lines = f.readlines()
# 关闭文件
f.close()
# 删除第一条数据
data_lines.pop(0)
# 将数据转换为字典，格式为：
# {年份:[[国家，gdp], [国家，gdp], ......], 年份：[[国家，gdp], [国家，gdp], ......], .......}
# 定义一个字典对象
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])  # 年份
    country = line.split(",")[1]  # 国家
    GDP = float(line.split(",")[2])  # GDP数据
    # 如何判断字典里有没有key呢？通过捕获异常的方法进行判断
    try:
        data_dict[year].append([country, GDP])  # 如果没有捕获到异常（字典里有该年份），就添加国家和Gdp
    except KeyError:
        data_dict[year] = []  # 如果捕获到这个异常（即缺少该年份），就构建一个空的列表
        data_dict[year].append([country, GDP])
print(data_dict)
# 创建时间线对象
timeline = Timeline({"theme": ThemeType.LIGHT})
# 排序年份
sorted_year_list = sorted(data_dict.keys())  # 取出字典对象里面的全部key，并进行排序
# for循环每一年的数据，基于每一年的数据，创建每一年的bar对象
for year in sorted_year_list:  # 针对每一年构建一个bar对象，并且添加到时间线里面
    # 把每一年里的数据按照GDP进行排序
    data_dict[year].sort(key=lambda element:element[1], reverse=True)
    # 只取GDP前8名的国家
    year_data = data_dict[year][0:8]
    # 构建柱状图
    x_data = []
    y_data = []
    for country_GDP in year_data:
        x_data.append(country_GDP[0])  # x轴添加国家
        y_data.append(country_GDP[1] / 100000000)  # y轴添加GDP数据
    # 构建柱状图对象
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP（亿）", y_data, label_opts=LabelOpts(position="right"))
    # 反转x轴和y轴
    bar.reversal_axis()
    # 设置每一年图表的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )
    timeline.add(bar, str(year))
# 设置时间线自动播放
timeline.add_schema(
    play_interval=1000,  # 设置播放时间，毫秒
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)
# 绘图
timeline.render("1960-2019全球GDP前8国家.html")
