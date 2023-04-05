# 导包
import requests
import re
import os

# 伪装信息，爬虫去请求网址，人家不会给你数据信息，伪装成正常的访问者
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"
}
name = input("请你输入你想采集的内容： ")
# https://image.baidu.com/search/index?tn=baiduimage&ie=utf-8&sid=&word=
# 网址的拼接
url = "https://image.baidu.com/search/index?tn=baiduimage&ie=utf-8&sid=&word=" + name
print(url)
# 发出请求
res = requests.get(url, headers=headers)
# 解析；获取当前页面所有的源代码 ； 图片数据都存在源代码里
html = res.content.decode()
# 筛选自己需要的图片
url_data = re.findall('"objURL":"(.*?)",', html)  # objURL是所有图片的前缀，其后是图片的地址
# print(url_data)

# 判断磁盘里面是否有img文件夹，如果没有就新建一个img的文件夹
if not os.path.exists('./img/'):
    os.makedirs('./img/')

num = 0
for b in url_data:
    num += 1
    img = requests.get(b)
    with open('./img/' + name + str(num) + '.jpg', 'ab') as f:
        f.write(img.content)
        print("--正在下载第" + str(num) + "张图片数据--")

