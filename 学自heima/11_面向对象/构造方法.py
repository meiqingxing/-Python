"""
演示类的构造方法
"""
# 演示使用构造方法对成员变量进行赋值
# 构造方法的名称： __init__
# 构造方法的作用： 构建类对象时会自动运行
# 构建类对象的传参会传递给构造方法，借此特性可以给成员变量赋值
# class Student:
#     # name = None
#     # age = None
#     # tel = None
#
#     def __init__(self, name, age, tel):  # 构造方法也是成员方法，不要忘记在参数列表中提供self
#         # 在构造方法内部定义成员变量，需要使用self关键字
#         # 变量是定义在构造方法内部，如果要成为成员变量，需要用self表示
#         self.name = name
#         self.age = age
#         self.tel = tel
#         print("Student类创建了一个对象！")
#
# stu = Student("周杰轮", 31, "122222233")
# print(stu.name)
# print(stu.age)
# print(stu.tel)

"""
练习案例
"""
# # 设计一个类，记录学生信息
# class Student:
#     name = None
#     age = None
#     place = None
#
#     def __init__(self, name, age, place):
#         for i in range(10):
#             print(f"当前录入第{i+1}位学生信息，总共需录入10位学生信息")
#             self.name = input("请输入学生姓名：")
#             self.age = int(input("请输入学生年龄："))
#             self.place = input("请输入学生地址：")
#             print(f"学生{i+1}信息录入完成，信息为：【学生姓名：{self.name}， 年龄：{self.age}， 地址：{self.place}】")
#
# stu = Student("周杰轮", 31, "北京")
class Student:
    def __init__(self, name, age, add):
        self.name = name
        self.age = age
        self.add = add
# 创建空字典，存放学生信息
stu_dict = {}
# for循环录入信息
for i in range(5):
    print(f"当前录入第{i+1}位学生信息，总共需录入5位学生信息")
    stu = Student(input("请输入学生姓名："), int(input("请输入学生年龄：")), input("请输入学生地址："))
    stu_dict[f"学生{i+1}"] = {}
    stu_dict[f"学生{i+1}"]["姓名"] = stu.name
    stu_dict[f"学生{i+1}"]["年龄"] = stu.age
    stu_dict[f"学生{i+1}"]["地址"] = stu.add
    print(f"学生{i+1}信息录入完成，信息为：【学生姓名：{stu.name}， 年龄：{stu.age}， 地址：{stu.add}】")
print("所有学生信息录入完成！！！")
print(stu_dict)