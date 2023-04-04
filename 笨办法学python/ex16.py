from sys import argv

script, filename = argv #用argv来获取一个文件名

print(f"We're going to erase {filename}.") #erase 擦除，清除
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename,'w') 
#用w这个额外的参数，说明你想用write模式来打开文件
# w表示用write模式打开文件；r表示read模式；a表示增补模式。后面还可能加修饰符
# 修饰符中最重要的就是+，‘w+’，‘r+’，‘a+’。其中open(filename)为‘r’模式

print("Truncating the file, Goodbye!")
target.truncate()  #清空文件

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")   #输入每一行的内容
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#rget.write(line3)
#target.write("\n")  #两种打印方式
target.write(line1+"\n"+line2+"\n"+line3+"\n")

print("And finally, we close it.")
target.close