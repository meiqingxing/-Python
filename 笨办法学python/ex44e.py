# 除了继承，还可以使用其他类和模块
# 通过调用模块中的函数来复制

class Other(object):  # 定义一个other的类

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")


class Child(object):  # 没有继承Other父类

    def __init__(self):  # self放在变量名第一个位置的占位词
        # 用来初始化一个类的新成员，当新成员创建时，这个函数会被自动调用
        self.other = Other()   # 这是什么意思？？用类other的成员对Child中的成员进行初始化？？

# self是一个指向对象的指针


    def implicit(self):
        self.other.implicit()  # 调用other类中的函数，而不是通过继承

    def override(self):  # 定义一个override函数
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()  # 调用
        print("CHILD, AFTER OTHER altered()")


son = Child()  # son是Child类的一个实例

son.implicit()
son.override()
son.altered()
