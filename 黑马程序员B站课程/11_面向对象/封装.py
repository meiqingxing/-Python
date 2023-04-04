"""
演示面对对象封装思想中私有成员的使用
"""

# 定义一个类，内含私有成员变量和私有成员方法
class Phone:

    __current_voltage = 0.5  # 当前手机运行电压

    def __keep_single_core(self):
        print("让CPU以单核模式运行")
    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话，并已经设置为单核运行以省电")

phone = Phone()
# phone.__keep_single_core()
# print(phone.__current_voltage)
phone.call_by_5g()
"""
何为封装？ 将现实事物在类中描述为属性和方法，即为封装。
现实事物有部分属性和行为是不公开对使用者开放的。同样在类中描述属性和方法的时候也需要达到这个要求，就需要定义私有成员。
如何定义？ 成员变量和成员方法的命名均以__作为开头即可
访问限制？ 类对象无法访问私有成员；；类中的其他成员可以访问私有成员
意义： 在类中提供仅供内部使用的属性和方法，而不对外开放（类对象无法使用）。
"""