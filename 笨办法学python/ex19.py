def cheese_and_crackers(cheese_count, boxes_of_crackers):  #定义函数，跳过解包过程，有两个参数
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get blanket.\n")
#创建函数：用def（define），函数名，加括号，括号里面放参数，参数用逗号隔开，加冒号

print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)  #直接给定两个数值，来为函数进行赋值
#调用函数：通过输入函数名称，加括号，括号里面放入想要的值

print("OR, we can use variables from our script:")
amount_of_cheese = 10    #定义两个变量，并赋值
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)   #通过变量的形式为函数赋值


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)  #通过数学运算的方式为函数的参数赋值


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
#赋值方式：数学运算和变量的结合