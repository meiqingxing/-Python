# from pygal.i18n import COUNTRIES  # 以前版本的代码
from pygal_maps_world.i18n import COUNTRIES


# # 测试国家和国别码的对应关系
# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])


def get_country_code(country_name):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    # 如果没有找到指定的国家，返回None
    return None


# # 测试
# print(get_country_code("Andorra"))
# print(get_country_code("United Arab Emirates"))
# print(get_country_code("Afghanistan"))
