class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

dad.implicit()
son.implicit()  # 隐式继承，调用父类定义的函数

dad.override()
son.override()  # 显式继承，子类定义函数对父类定义的函数进行覆盖

dad.altered()
son.altered()  # 利用Python内置的函数super(),获取父类
