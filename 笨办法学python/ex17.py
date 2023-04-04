from sys import argv
from os.path import exists
#import可以调用海量的代码

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line,how?
#in_file = open(from_file)
indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long")
#len（）取字符串的长度，然后返回一个数字

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to contine, CTRL-C to about.")
input()
#exists命令：基于一个字符串里面的变量文件名来判断；如果一个文件存在返回True，不存返回False 

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
#in_file.close()




