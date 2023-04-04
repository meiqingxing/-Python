""""
演示基础柱状图的开发
"""
# 导入模块
from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType
# # 使用bar构建基础柱状图
# bar = Bar()
# # 添加x轴
# bar.add_xaxis(["中国", "美国", "英国"])
# # 添加y轴
# bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
# # 反转x轴和y轴
# bar.reversal_axis()
# # 设置数值标签在右侧
#
# # 绘图
# bar.render("基础柱状图.html")

"""
演示带有时间线的柱状图的开发
"""
bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [40, 30, 30], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP", [50, 25, 20], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

bar4 = Bar()
bar4.add_xaxis(["中国", "美国", "英国"])
bar4.add_yaxis("GDP", [70, 50, 10], label_opts=LabelOpts(position="right"))
bar4.reversal_axis()
# 构建时间线对象
timeline = Timeline()
# 在时间线内添加柱状图对象
timeline.add(bar1, "点1")
timeline.add(bar2, "点2")
timeline.add(bar3, "点3")
timeline.add(bar4, "点4")
# 设置自动播放
timeline.add_schema(
    play_interval=1000,  # 设置自动播放的时间间隔，单位毫秒
    is_timeline_show=True,  # 是否在自动播放的时候，显示时间线
    is_auto_play=True,  # 是否自动播放
    is_loop_play=True,  # 是否循环自动播放
)
# # 主题设置（颜色等）
# timeline = Timeline(
#     {"theme": ThemeType.DARK}
# )
# 绘图是用时间线对象绘图，而不是bar对象了
timeline.render("基础时间线柱状图.html")