"""
规则表达式，时使用单个字符串来描述、匹配某个句法规则的字符串，常被用来检索、替换那些符合某个模式（规则）的文本。
简单来说：字符串定义规则，并通过规则去验证字符串是否匹配。

python正则表达式，使用re模块，并基于re模块中的三个基础方法来做正则匹配：match、search、findall
re.match(匹配规则，被匹配字符串)
从被匹配字符串开头进行匹配，匹配成功返回匹配对象（包含匹配的信息），匹配不成功返回空。

re.search(匹配规则，被匹配字符串)
搜索整个字符串，找出匹配的。从前向后，找到第一个后，就停止，不会继续向后；整个字符串找不到，返回None。

findall(匹配规则，被匹配字符串）
匹配整个字符串，找出全部匹配项；找不到返回空list:[]
"""
# 导包
import re

# match 从头匹配；头部没有发现，就返回None
s = "python itheima python "
result = re.match("python", s)
print(result)
print(result.span())
print(result.group())

# search 搜索匹配
result = re.search("python1", s)
print(result)

# findall 搜索全部匹配
result = re.findall("python", s)
print(result)
