"""
演示变量的类型注解
使用： 无法直接看出变量类型之时，添加变量的类型注解
"""
import random
import json

# 基础数据类型注解;  一般没有意义
var_1: int = 10
var_2: float = 10.1
var_3: str = "itheima"
var_4: bool = True

# 类对象类型注解
class Student:
    pass
stu: Student = Student()

# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"itheima": 666}

# 容器类型详细注解
your_list: list[int] = [12, 13, 14]
your_tuple: tuple[int, str, bool] = (1, "itheima", True)  # 要对元组的每一个元素进行注解
your_dict: dict[str, int] = {"itheima": 666}  # 注解两个就行，字典的key和value

# 在注释中进行类型注解
var_11 = random.randint(1, 10)  # type: int
var_22 = json.loads("{'name': 'zhangsan'}")  # type: dict[str, str]
def func():
    return 10
var_33 = func()  # type: int

# 类型注解的限制
# 仅仅只是提示，并不会真正对类型做验证和判断