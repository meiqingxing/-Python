from sys import argv
#通过argv来获取文件名
script, filename = argv

txt = open(filename)   #不会返回文件内容，类似创建一个文件对象

print(f"Here's your file {filename}:")
print(txt.read())    #读取文件的内容

print("Type the filename again:")
file_again = input(">")   #打印用户提示符

txt_again = open(file_again)

print(txt_again.read())

#close 关闭文件
#read 读取文件内容，可以把读取结果赋给一个变量
#readline 只读取文本文件的一行内容
#truncate 清空文件
#write('stuff') 给文件写入一些东西
#seek() 把读/写的位置移到文件的最开头