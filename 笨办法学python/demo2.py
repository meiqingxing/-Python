#转义字符的使用
print('hello\nworld!')  #\ + 转义字符的首字母  n——newline
print('hello\tworld!')  # t——table，一个制表位，一般四个空格
print('hello\rworld!')    #return   world将hello进行覆盖
print('hello\bworld!')   #退一个格
print('\n')

print('http:\\www.baidu.com')
print("http:\\\\www.baidu.com")
print('老师说：\'你们好\'')
print('\n')

#原字符，不希望转义字符起作用，在字符串前加r或R
print('hello\nworld!')
print(r'hello\world!')  #最后一个字符不能是"\"
print('\n')

name = ('Arcmia')
print(name)
print('标识符',id(name))
print('类型',type(name))
print('值',name)