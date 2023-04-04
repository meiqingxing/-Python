"""
进程： 程序在操作系统内运行，即成为一个运行进程。
操作系统中可以运行多个进程，即多任务运行，称为多任务并行执行。
线程： 程序内部可以有多个线程，程序的运行本质上就是由进程内部的线程在实际工作的。
一个进程内可以运行多个线程，即多线程运行。
注意点：
进程之间是内存隔离的，不同的进程拥有各自的内存空间。  类似于不同的公司拥有不同的办公场所。
线程之间是内存共享的，线程是属于进程的，一个进程内的多个线程之间是共享这个进程所拥有的内存空间的。  就好比公司员工之间是共享公司的办公场所。

并行执行：同一时间做不同的工作
进程之间就是并行执行的，线程也可以并行执行。像这样一个程序在同一时间做两件乃至多件不同的事情，称之为：多线程并行执行
"""
# 通过threading模块来实现
import threading
import time
# thread_obj = threading.Thread([group [, target [, name [, args [, kwargs]]]]])
"""
- group : 暂时无用，未来功能的预留参数
- target：执行的目标任务名
- args： 以元组的方式给执行任务传参
- kwargs： 以字典方式给执行任务传参
- name： 线程名，一般不用设置
"""
def sing(msg):
    while True:  # 无限循环
        print(msg)
        time.sleep(1)

def dance(msg):
    while True:  # 无限循环
        print(msg)
        time.sleep(1)

if __name__ == "__main__":
    # 创建一个唱歌的线程
    sing_thread = threading.Thread(target=sing, args=("我要唱歌，哈哈哈...", ))  # 通过元组传参
    # 创建一个跳舞的线程
    dance_tread = threading.Thread(target=dance, kwargs={"msg": "我在跳舞，啦啦啦..."})  # 通过字典传参

    # 让线程去干活吧
    sing_thread.start()
    dance_tread.start()


