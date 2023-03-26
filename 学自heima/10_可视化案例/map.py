"""
演示地图可视化的基本应用
"""
# 基础地图
# from pyecharts.charts import Map
# from pyecharts.options import VisualMapOpts
# # 准备地图对象
# map = Map()
# # 准备数据
# data = [
#     ("北京", 99),
#     ("上海", 199),
#     ("湖南", 299),
#     ("台湾", 399),
#     ("广东", 499)
# ]
# # 添加数据
# map.add("测试地图", data, "china")
# # 设置全局选项
# map.set_global_opts(
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         pieces=[
#             {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
#             {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
#             {"min": 100, "max": 500, "label": "100-500", "color": "#990000"}
#         ]
#     )
# )
# # 绘图
# map.render()

# 全国疫情可视化地图
import json
from pyecharts.charts import Map
from pyecharts.options import *
# 读取数据文件
f = open("E:\Python学习资料\黑马资料\可视化案例数据\地图数据\疫情.txt", "r", encoding="UTF-8")
data = f.read()  # 读取全部数据
# 关闭文件
f.close()
# 取到各省数据
# 将字符串json数据转换为python的字典
data_dict = json.loads(data)  # 基础数据字典
# 从字典中取出省份的数据
province_data_list = data_dict["areaTree"][0]["children"]
# 组装每个省份和确诊人数为元组，并各个省的数据都封装入列表内
data_list = []  # 绘图需要的数据列表
for province_data in province_data_list:
    province_name = province_data["name"]  # 省份名称
    province_confirm = province_data["total"]["confirm"]  # 确诊人数
    data_list.append((province_name, province_confirm))
print(data_list)
# 创建地图对象
map = Map()
# 添加数据
map.add("各省份确诊人数", data_list, "china")
# 设置全局配置，定制分段的视觉映射
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min": 1, "max": 99, "lable": "1-99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "lable": "100-999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "lable": "1000-4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "lable": "5000-9999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "lable": "10000-99999人", "color": "#CC3333"},
            {"min": 100000, "lable": "100000+", "color": "#990033"},
        ]
    )
)
# 绘图
map.render("全国疫情地图.html")