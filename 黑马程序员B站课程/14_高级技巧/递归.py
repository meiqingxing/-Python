"""
递归：即方法（函数）自己调用

演示Python递归操作
需求：通过递归，找出一个指定文件夹内的全部文件
思路：写一个函数，列出文件夹内的全部内容，如果是文件就收集到list
     如果是文件夹，就递归调用自己，再次判断。
"""
# 导包
import os

def test_os():
    """
    演示os模块的3个基础方法
    :return: None
    """
    print(os.listdir("E:\Python学习资料\第16章资料/test"))  # 把文件夹里面的内容列出来
    print(os.path.isdir("E:\Python学习资料\第16章资料/test/a"))  # 判断你给的路径是否是一个文件夹；是，True；否，返回False
    print(os.path.exists("E:\Python学习资料\第16章资料/test"))  # 判断指定路径是否存在；是，True；否，返回False


def get_files_recursion_from_dir(path):
    """
    从指定的文件夹中使用递归的方式，获取全部的文件列表
    :param path: 被判断的文件夹
    :return: list，包含全部的文件，如果目录不存在或者无文件就返回一个空list
    """
    print(f"当前判断的文件夹是“{path}")
    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + "/" + f
            if os.path.isdir(new_path):
                # 进入到这里，表明这个目录是文件夹不是文件
                file_list += get_files_recursion_from_dir(new_path)  # 递归，调用自己 ；关键代码，递归调用的返回值要加上
            else:
                file_list.append(new_path)  # 注意退出的条件，否则容易变成无限递归
                                            # 注意返回值的传递，确保从最内层，层层传递到最外层
    else:
        print(f"指定的目录{path}，不存在")
        return []

    return file_list



if __name__ == "__main__":
    test_os()
    print(get_files_recursion_from_dir("E:\Python学习资料\第16章资料/test"))
