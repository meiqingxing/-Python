"""
复写父类成员属性和成员方法
复写：对父类的成员属性和成员方法进行重新定义
注意！只可以在子类内部调用父类的同名成员，子类的实体类对象调用默认是调用子类复写的
"""
# 定义父类
class Phone():
    IMEI = None
    producer = "HM111"
    def  call_by_4g(self):
        print("4G通话")

# 定义子类，复写父类成员
class My_phone:
    producer = "ITHEIMA"  # 复写父类的成员属性
    def call_by_4g(self):
        print("开启CPU单核模式，确保通话的时候省电")
        # 在子类中，调用父类成员
        # 方式1：父类名.成员属性；父类名.成员方法(self)
        print(f"父类的厂商是:{Phone.producer}")
        Phone.call_by_4g(self)
        # 方式2：super().成员属性；super().成员方法()
        # print(f"父类的厂商是:{super().producer}")
        # super().call_by_4g()
        # print("使用4g网络进行通话")
        print("关闭CPU单核模式，确保性能")

phone = My_phone()
phone.call_by_4g()
print(phone.producer)
