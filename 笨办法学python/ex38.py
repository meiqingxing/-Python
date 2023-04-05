ten_things = "Apples Oranges Crows Telephone Light Surge"

print("Wait there are not 10 things in that list. Let's fix it.")

stuff = ten_things.split(' ')  #对ten_things变量里面的字符串进行分割
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()  #用pop函数获取more_stuff列表里面的元素，并储存在next_one变量中
    print("Adding: ", next_one)   #上一行中，其实是pop(more_stuff)
    stuff.append(next_one)
    print(f"There arte {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff .")

print(stuff[1])   #打印stuff列表中第2个元素
print(stuff[-1])  #whoa! fancy   #打印列表中倒数第一个元素
print(stuff.pop())
print(' '.join(stuff)) #what? cool!  #join是一种可以调用的方法，他能够把字符串放在列表的元素之间，把它们连接起来
                       #把列表里面的元素拿出来，并用空格连接起来成为字符串
print('#'.join(stuff[3:5]))  #super stellar!  #切片，切出3和4，并用#连接起来

