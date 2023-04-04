"""
多态： 多种状态，即完成某个行为时，使用不同的对象会得到不同的状态
常用在继承关系上：以父类做定义声明，以子类做实际工作，用以获得同一行为的不同状态
演示面向对象的多态特性以及抽象类（接口）的使用
抽象类的作用：多用于做顶层设计，以便子类做具体实现；也是对子类的一种软性约束，要求子类必须复写父类的一些方法，并且配合多态使用，获取不同的工作状态
"""
# 定义父类
class Animal:
    def speak(self):
        # 父类用来确定有哪些写法，具体的方法实现，由子类自行决定
        # 抽象类（接口）： 含有抽象方法的类称为抽象类
        # 抽象方法：方法体是空实现（pass）的称之为抽象方法
        pass
# 定义子类
class Dog(Animal):
    def speak(self):
        print("wangwangwang")
# 定义子类
class Cat(Animal):
    def speak(self):
        print("miaomiaomaio")

def make_noise(animal: Animal):  # :Animal是类型注解，声明传入的是父类对象
    """制造点噪音，需要传入Animal对象"""
    animal.speak()
# 演示多态，使用2个子类对象来调用函数
dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)

# 演示抽象类
class AC:  # 父类做顶层设计
    def cool_wind(self):
        """制冷"""
        pass
    def warm_wind(self):
        """制热"""
        pass
    def swing_l_r(self):
        """左右摆风"""
        pass

class Midea_AC(AC):  # 子类做具体实现
    def cool_wind(self):
        print("美的空调制冷")
    def warm_wind(self):
        print("美的空调制热")
    def swing_l_r(self):
        print("美的空调左右摆风")
class GREE_AC(AC):  # 子类做具体实现
    def cool_wind(self):
        print("格力空调制冷")
    def warm_wind(self):
        print("格力空调制热")
    def swing_l_r(self):
        print("格力空调左右摆风")

# 定义函数（方法），通过类型注解声明需要父类对象，实际传入子类对象进行工作，从而获得不同的工作状态
def make_cool(ac: AC):
    ac.cool_wind()
def make_warm(ac: AC):
    ac.warm_wind()
def make_swing(ac: AC):
    ac.swing_l_r()

midea_ac = Midea_AC()
gree_ac = GREE_AC()

make_cool(midea_ac)  # 实际向函数传入子类对象