"""RDD
演示RDD的map方法的使用
map算子，将RDD的数据一条条处理（处理的逻辑 基于map算子中接受的处理函数），返回新的RDD
"""
# 导包
from pyspark import SparkConf, SparkContext
import os
os.environ['JAVA_HOME'] = "C:\Program Files\Java\jdk-19"  # 告诉Pycharm哪里找到java环境变量
os.environ['PYSPARK_PYTHON'] = "D:\Python3.92\python.exe"  # 告诉PySpark哪里能找到Python解释器

# 创建SparkConf对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf=conf)
# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])
# 通过map方法将全部数据都乘以10
# def func(data):
#     return data * 10
# rdd2 = rdd.map(func)  # (T) -> U
# 函数很简单，可以用lambda匿名函数
rdd2 = rdd.map(lambda x: x * 10).map(lambda x: x + 5)
print(rdd2.collect())
# rdd3 = rdd2.map(lambda x: x + 5)
# 上面一行有点复杂，可以链式调用的方式多次调用算子

"""
flatMap算子：对rdd执行map操作，计算逻辑与map一模一样，就多出了解除嵌套操作

"""
rdd4 = sc.parallelize(["itheima itcast 666", "itheima itheima itcast", "python itheima"])
# 需求，将RDD数据中的单词一个个提取出来
# rdd5 = rdd4.map(lambda x: x.split(" "))  # 单词虽然被切分，但是依旧在各个list中
rdd5 = rdd4.flatMap(lambda x: x.split(" "))  # 单词被切分，所有单词在一个list中
print(rdd5.collect())
