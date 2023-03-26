"""
在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数，我们把这个使用外部函数变量的内部函数称为闭包。
达到目的：既想依赖外部全局变量，又不想全局变量被修改
优点：
1. 无需定义全局变量即可实现通过函数，持续访问、修改某个值
2. 闭包使用的变量的所用于在函数内，难以被错误的调用修改
缺点：
由于内部函数持续引用外部函数的值，所以会导致这一部分内存空间不被释放，一只占用内存。
"""
# 简单演示

# logo = "黑马程序员"  ；将变量作用在函数外，在调用函数时需要用到这个变量；当不调用函数时，这个变量不发挥作用但是依旧存在
def outer(logo):

    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")

    return inner

fn1 = outer("黑马程序员")
# 黑马程序员对于函数inner()来说持续存在，对于outer()来说，是临时存在；对于inner()来说是外部，对于outer()来说是内部
# 现在实现的目标对于内层inner()函数所依赖的外部变量，调用几次黑马程序员，都存在；但是黑马程序员这个外部变量，不能被访问和修改
# 因为黑马程序员这个logo变量对于outer()函数来说，是内部临时变量
fn1("大家好")
fn1("大家好")

fn2 = outer("传智教育")  # 如果想修改黑马程序员这个logo变量，只能再次调用outer()函数，传入不同的logo参数
fn2("大家好")

"""
修改外部函数变量值：
加入nonlocal关键字，修饰外部函数的变量才可以在内部函数中修改外部函数变量的值
在闭包函数（内部函数中）想要修改外部函数的变量值，需要用nonlocal声明这个外部变量
"""
# 示例
# num1 = 11  # 全局变量，代码复杂之后，很容易在import等过程中被窜改
def num_outer(num1):  # 不是全局变量，是作用在函数内部的临时变量，不容易被修改

    def num_inner(num2):
        nonlocal num1  # 也是全局变量，相对于函数num_inner()来说
        num1 += num2
        print(num1)

    return num_inner

fn = num_outer(10)
fn(10)
fn(10)
fn(10)

print("-------------------------")

# 使用闭包实现ATM小案例
def account_create(fund_money = 0):

    def atm(check_money, Yes_or_Not = True):
        nonlocal fund_money
        if Yes_or_Not:
            fund_money += check_money
            print(f"存款 + {check_money}, 余额为：{fund_money}.")
        else:
            fund_money -= check_money
            print(f"取款 - {check_money}, 余额为：{fund_money}.")

    return atm

money = account_create(1000)
money(200)
money(400, Yes_or_Not=False)
