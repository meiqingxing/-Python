"""
演示面向对象类中的成员方法定义和使用
"""
# 函数是写在类外面的，方法是指定义在类内部的
# 类的属性：称为成员变量
# 类的行为：称为成员方法

# 定义一个带有成员方法的类
class Student:
    name = None  # 学生的名字

    def say_hi(self):
        # self必须要有；作用：表示类对象本身；只有通过self，成员方法才能访问成员变量
        print(f"大家好！我是{self.name}，欢迎大家多多关照！！！")
        # name作为成员变量，say_hi作为成员方法，想在成员方法内访问成员变量，必须要使用self.***

    def say_hi2(self, msg):  # 看起来两个参数
        print(f"大家好，我是：{self.name}, {msg}")
        # 访问msg，他是外部传入的，直接用就行，不需要self.***

stu = Student()
stu.name = "李华"
stu.say_hi()   # 不需要传参
stu.say_hi2("唉哟，不错哟！")  # 实际上只传入一个，只传入msg
stu2 = Student()
stu2.name = "周杰轮"
stu2.say_hi2("小伙子我看好你")