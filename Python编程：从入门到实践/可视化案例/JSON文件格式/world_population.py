"""
缺少数据
"""
import json
from countries import get_country_code

# 将数据加载到列表中
filename = "population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

# 打印每个国家2010年的人口数量
for pop_dict in pop_data:  # 从列表的第0个元素开始，每个元素都是字典
    if pop_dict["Year"] == '2010':
        country_name = pop_dict["Country Name"]
        # JSON中的每个键值对都是字符串
        population = int(float(pop_dict["Value"]))
        # print(country_name + ": " + str(population))

        code = get_country_code(country_name)
        if code:
            print(code + ": " + str(population))
        else:
            print("ERROR - " + country_name)