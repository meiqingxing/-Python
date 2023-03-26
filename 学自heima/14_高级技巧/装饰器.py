"""
装饰器：
创建一个闭包函数，在闭包函数内调用目标函数
其实也是一种闭包，功能就是：在不破坏目标函数原有的代码和功能的前提下，为目标函数增加新功能。
"""

# # 装饰器的一般写法（闭包）
# def outer(func):              # 定义一个闭包函数，接收包装函数的传入，在闭包函数内部：
#     def inner():              # 执行目标函数
#         print("我要睡觉了")
#         func()                # 调用包装函数，完成功能的添加
#         print("我要起床了")
#
#     return inner
#
# def sleep():
#     import random
#     import time
#     print("睡眠中.......")
#     time.sleep(random.randint(1, 5))
#
# fn = outer(sleep)  # 调用outer()，传入sleep函数（把需要被包装的函数作为参数传递），返回的是inner()函数
# fn()  # 调用inner()：print、sleep()、print


# 装饰器的快捷写法（语法糖）；使用@outer，定义在目标函数sleep()之上
def outer(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我要起床了")

    return inner


@outer
def sleep():
    import random
    import time
    print("睡眠中.......")
    time.sleep(random.randint(1, 5))

sleep()