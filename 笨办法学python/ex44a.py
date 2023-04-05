class Parent(object):

    def implicit(self):
        print("PARENT implicit()")


class Child(Parent):
    pass  # 告知Python需要一个空块的方式，这样就创建了一个名为Child的类，但是没有什么新内容需要定义；但是他会继承父类的所有行为


dad = Parent()
son = Child()

# Parent().implicit()
dad.implicit()
son.implicit()  # 调用函数，即使Child中没有定义一个隐式函数，仍然可以正常运行，因为它调用了Parent中定义的那个函数

#  把函数放在基类中，所有的子类会自动获得这些特性，对于需要些重复代码的类来说十分方便

