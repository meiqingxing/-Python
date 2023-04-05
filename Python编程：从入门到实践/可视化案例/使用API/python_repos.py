"""
执行API调用并处理结果，找出GitHub上星级最高的Python项目

"""
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


"""
本来报错：
requests.exceptions.SSLError: HTTPSConnectionPool(host='api.github.com', port=443): Max retries exceeded with url: /search/repositories?q=language:python&sort=stars (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1123)')))
但是安装了三个requests的依赖包即可解决问题：
pip install cryptography
pip install pyOpenSSL
pip install certifi
或者：
# import certifi
# import urllib3
# http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
如果问题还存在，关掉代理
"""

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)  # 调用get()并将url传递，将响应对象存储在变量r中
print("Status code: ", r.status_code)  # 查看请求是否成功（状态码200表示请求成功）

response_dict = r.json()  # API返回JSON格式数据，并将其转换为字典
print(response_dict.keys())  # API返回数据的key
print("Total repositories:", response_dict['total_count'])  # 共包含多少个Python仓库


# 探索有关仓库的信息
repo_dicts = response_dict['items']  # 与items关联的值是一个列表，其中包含许多字典，每个字典都包含一个python仓库的信息
print("Repositories returned:", len(repo_dicts))


# # 研究第一个仓库
# repo_dict = repo_dicts[0]  # 第一个仓库
# print("\nkeys:", len(repo_dict))  # 查看键数，可知有多少信息
# for key in sorted(repo_dict.keys()):  # 遍历key，可知信息涉及什么
#     print(key)
# # 提取与键相关联的值
# print("\nSelected information about first repository:")
# print('Name:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])  # 项目所有者的登录名
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Created:', repo_dict['created_at'])
# print('Updated:', repo_dict['updated_at'])
# print('Description:', repo_dict['description'])

# # 概述最受欢迎的仓库
# print("\nSelected information about each repository:")
# for repo_dict in repo_dicts:
#     print('\nName:', repo_dict['name'])
#     print('Owner:', repo_dict['owner']['login'])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Description:', repo_dict['description'])

# names, stars = [], []  # 名字作为条形标签，星数作为条形高度
names, plot_dicts = [], []  # 名字作为条形标签，plot_dicts提供工具提示信息
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        "value": repo_dict['stargazers_count'],  # 存储星数
        "label": repo_dict['description'],  # 存储项目描述
        'xlink': repo_dict['html_url']  # 将每个条形转换为可以访问的网站链接
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)  # 设置样式

my_config = pygal.Config()  # 创建一个pygal类Config的实例，通过修改其属性来定制图表的外观
my_config.x_label_rotation = 45  # 标签绕x轴旋转45°
my_config.show_legend = False  # 隐藏图例
my_config.title_font_size = 24  # 标题大小
my_config.label_font_size = 14  # 副标签：x轴上的项目名及y轴上的大部分数字
my_config.major_label_font_size = 18  # 主标签：y轴上为5000整数倍的刻度
my_config.truncate_label = 15  # 将较长的项目名缩短为15个字符
my_config.show_y_guides = False  # 隐藏图表中的水平线
my_config.width = 1000  # 图表宽度

# 创建条形图
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)  # 不需要给数据列表添加标签: ''
chart.render_to_file('python_repos.svg')

