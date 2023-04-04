"""
内含私有成员方法的类的练习
"""
# 设计一个手机类
class Phone():
    # 定义私有成员变量，类型为bool
    __is_5g_enable = bool   # 设置5g状态

    # 定义私有成员方法，对私有成员变量进行判断
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")

    # 定义公开成员方法，可以访问类中的私有成员方法
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

user = Phone()
user.call_by_5g()  # 类对象可以使用公开成员方法