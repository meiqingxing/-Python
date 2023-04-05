class Parent(object):

    def override(self):
        print("PARENT override()")


class Child(Parent):

    def override(self):
        print("CHILD override()")


dad = Parent()
son = Child()

# Parent().override()
# Child().override()
dad.override()  # dad是Parent的一个实例
son.override()  # son是Child的一个实例，调用的函数通过Child自己定义的版本重写了函数
