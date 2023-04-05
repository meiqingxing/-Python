"""
执行API调用并处理结果，找出GitHub上星级最高的Python项目

"""
import requests

"""
本来报错：
requests.exceptions.SSLError: HTTPSConnectionPool(host='api.github.com', port=443): Max retries exceeded with url: /search/repositories?q=language:python&sort=stars (Caused by SSLError(SSLEOFError(8, 'EOF occurred in 
但是安装了三个requests的依赖包即可解决问题：
pip install cryptography
pip install pyOpenSSL
pip install certifi
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

# 概述最受欢迎的仓库
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])


