#this one is like your scripts with argv
def print_two(*args):   #创建函数方法1   #*号的作用就是告诉Python取所有的参数给函数，不常用（除非特殊需要）
    arg1, arg2 = args  #解包参数argument
    print(f"arg1: {arg1}, arg2: {arg2}")   #打印参数

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):   #创建函数方法2，跳过整个解包参数
    print(f"arg1: {arg1}, arg2:{arg2}")

#this just takes one argument
def print_one(arg1):   #只用一个参数创建函数
    print(f"arg1: {arg1}")

#this one takes no arguments
def print_none():     #创建没有参数的函数
    print("I got nothin'.")


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()