"""
Hacker News网站，用户分享编程和技术方面的文章
Hacker News的API让你能够访问有关该网站所有文章和评论的信息，且不要求你通过注册获得密钥。
例如：https://hacker-news.firebaseio.com/v0/item/9884165.json
"""

import requests
from operator import itemgetter

# 执行API调用并存储响应对象，打印响应状态
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)  # API调用返回一个列表，其中包含当前最热门的500篇文章的ID
print("Status code:", r.status_code)

# 处理有关每篇文章的信息
submission_ids = r.json()  # 将响应文本转换为列表
submission_dicts = []
for submission_id in submission_ids[:10]:  # 前30篇
    # 对于每篇文章，都执行一个API调用
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)  # 打印状态
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],  # 标题
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),  # 链接
        'comments': response_dict.get('descendants', 0)
        # 评论次数：不确定某个键是否包含在字典中时，可使用方法dict.get()，它在指定的键存在时返回与之相关联的值，并在指定的键不存在时返回你指定的值（这里是0）。
        }
    submission_dicts.append(submission_dict)


submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)  # 进行排序，通过comments；降序排列

for submission_dict in submission_dicts:  # 遍历
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])

