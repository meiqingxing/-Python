"""
演示Union联合类型注解
"""
# 使用Union类型，必须先导包
from typing import Union

my_lsit: list[Union[int, str]] = [1,2, "itheima", "itcast"]
my_dict: dict[str, Union[int, str]] = {"name": "itheima", "age": 11}

def func(data: Union[int, str]) -> Union[int, str]:
    return data

print(func(1))