class Parent(object):

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def altered(self):  # 定义子类的同名函数版本
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()  # super() Python的内置函数，可以调用父类的函数版本
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

# Parent().altered()
# Child().altered()
dad.altered()
print("\n")
son.altered()
