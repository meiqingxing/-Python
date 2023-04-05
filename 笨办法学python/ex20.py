from sys import argv  #调用argv

script, input_file = argv  #获取一个参数

def print_all(f):   #定义函数,读出文件里的内容
    print(f.read())

def rewind(f):   #定义函数，seek()函数处理的是字节，不是行。
    f.seek(0)  #seek(0)把文件移动到0字节（最开始处）

def print_a_line(line_count, f):
    print(line_count, f.readline())  #readline()里面的代码能够扫描文件的每个字节，当他发现\n字符，就会停止
    #这个文件，然后回到他发现的地方

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")  #翻译：现在让我们倒带，有点像磁带。

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1  #+=是一种缩写,举例：x = x+y等价于x += y
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

#readline()函数返回文件中每行最后的\n，又在print函数的结尾加上一个end=' '来避免给每行加上两个\n。
#所以打印出来行之间会有空行