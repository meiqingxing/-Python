"""
设计模式：
编程套路，可以极大地方便程序的开发
最常见、最经典的设计模式，就是所学习的面向对象，除此之外还有既定套路：单例、工厂模式...
"""

"""
单例模式
效果：某些场景下，一个类无论获取多少次类对象，都仅仅提供一个具体的实例，用以节省创建类对象的开销和内存开销
定义：保证一个类只有一个实例，并提供一个访问它的全局访问点
"""
# from str_tools import StrTools
#
# s1 = StrTools
# s2 = StrTools
#
# print(id(s1))
# print(id(s2))  # 两个id地址一样

"""
工厂模式
当需要大量创建一个类的实例的时候，可以使用工厂模式。
优点：大批量创建对象的时候有统一的入口，易于代码维护；当发生修改，仅修改工厂类的创建方法即可；符合现实世界的模式，即由工厂来制作产品（对象）
"""
class Person:
    pass
class Worker(Person):
    pass
class Student(Person):
    pass
class Teacher(Person):
    pass

# # 之前的获取类对象的方法
# worker = Worker()
# stu = Student()
# teacher = Teacher()

class PersonFactory:  # 创建一个额外的工厂类，调用方法的形式去获得你想要的对象

    def get_person(self, p_type):
        if p_type == 'w':
            return Worker()
        elif p_type == 's':
            return Student()
        else:
            return Teacher()

pf = PersonFactory()
worker = pf.get_person('w')
stu = pf.get_person('s')
teacher = pf.get_person('t')