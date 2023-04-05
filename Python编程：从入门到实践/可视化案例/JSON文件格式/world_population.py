"""
缺少数据
"""
import json
from countries import get_country_code
import pygal_maps_world.maps
from pygal.style import RotateStyle  # 调整颜色，指定基色
from pygal.style import LightColorizedStyle  # 加亮地图的颜色，修改整个图表的主题


# 将数据加载到列表中
filename = "population_data.json"  # 缺失文件，仅起熟练代码作用
with open(filename) as f:
    pop_data = json.load(f)

# 创建一个包含人口数量的字典
cc_populations = {}
for pop_dict in pop_data:  # 从列表的第0个元素开始，每个元素都是字典
    if pop_dict["Year"] == '2010':
        country_name = pop_dict["Country Name"]
        code = get_country_code(country_name)  # 获取国别码

        # JSON中的每个键值对都是字符串，需要转换为数值
        population = int(float(pop_dict["Value"]))
        # print(country_name + ": " + str(population))

        if code:
            cc_populations[code] = population  # 字典向向key输入value

        else:
            print("ERROR - " + country_name)

# 根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():  # 遍历cc_populations字典
    if pop < 10000000:
        cc_pops_1[cc] = pop  # 将{国别码：人口数量}键值对添加到对应组的字典
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 看看每组分别包含多少个国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

# wm_style = LightColorizedStyle  # 不能直接控制使用的颜色，Pygal将选择默认的基色
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
# #XXXXXX:十六位进制的RGB颜色，少量red，中量green，多量blue；将LightColorizedStyle作为基本样式，设置较亮的主题

wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
# 每个组中，国家按照人口数量从少到多以从浅到深的颜色区别
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')
