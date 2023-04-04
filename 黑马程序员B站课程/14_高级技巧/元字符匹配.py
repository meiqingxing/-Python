"""
演示Python正则表达式使用元字符进行匹配
"""
# 导包
import re
s = "itheima @@pythonHHHHH1110 ! ksd;bad666 @#$ itcast336"

"""
单字符匹配
"""
# \d ：匹配数字，即0-9
result = re.findall(r'\d', s)  # 字符串前面带上r的标记，表示字符串中转义字符无效，就是普通字符的意思。
print(result)

# \W ：匹配非单词字符
result = re.findall(r'\W', s)
print(result)

# [] ：匹配[]中列举的字符
result = re.findall(r'[a-zA-Z]', s)  # r'[a-zA-Z09]'  r'[aceEDG1203]'
print(result)

"""
数量匹配、 边界匹配、分组匹配
"""
# 匹配账号，只能由字母和数字组成，长度限制6-10位
r = '^[0-9a-zA-Z]{6,10}$'  # 注意：逗号后面不要写空格   ^：匹配字符串开头    $：匹配字符串结尾
s = "1654feg"
print(re.findall(r, s))

# 匹配qq号，要求纯数字，长度5-11，第一位不为0
r = '^[1-9][0-9]{4,10}$'
s = "55165168"
print(re.findall(r, s))

# 匹配邮箱地址，只允许qq、163、gmail这三种邮箱地址
r = r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'
s = 's.c.v.d.d.ev.sdsfe@qq.s.d.f.eg.e.d'
# print(re.findall(r, s))  # 使用findall注意：如果正则表达式里面有()分组，他就会把每一个组的结果给你列出来；可以把正则的整体加()，变成一个组
print(re.match(r, s))
