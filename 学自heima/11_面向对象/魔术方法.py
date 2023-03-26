"""
演示其他内置方法
"""
class Student:
    # 构造方法，可用于创建类对象的时候设置初始化行为
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__魔术方法  ; 由输出内存地址转变为输出字符串
    def __str__(self):
        return f"Student类对象, name:{self.name}, age:{self.age}"

    # __lt__ 小于符号比较方法：两个类对象进行小于或大于比较
    def __lt__(self, other):
        return self.age < other.age

    # __le__ 小于等于符号比较方法：两个类对象进行小于等于或大于等于比较
    def __le__(self, other):
        return self.age <= other.age

    # __eq__ 相等比较方法：用于两个类对象进行相等比较；如果没有这个方法，则比较的是内存地址
    def __eq__(self, other):
        return self.age == other.age

stu1 = Student("周杰轮", 31)
print(stu1)
print(str(stu1))

stu2 = Student("林俊杰", 35)
print(stu1 < stu2)
print(stu1 > stu2)

print(stu1 <= stu2)
print(stu1 >= stu2)