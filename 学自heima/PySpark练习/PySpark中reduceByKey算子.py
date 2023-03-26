"""
reduceByKey算子：针对KV型RDD，自动按照key分组，然后根据你提供的聚合逻辑，完成组内数据（value）的聚合操作
KV型RDD：其实就是二元元组(('a', 1), ('b', 2))
key分组：把二元中的第一个作为key，如a, b
用法：
    rdd.reduceByKey(func)
    # func: (v, v) -> v
    # 接受2个传入参数（类型要一致），返回一个返回值，类型和传入要求一致
"""
from pyspark import SparkConf, SparkContext
import os
os.environ['JAVA_HOME'] = "C:\Program Files\Java\jdk-19"  # 告诉Pycharm哪里找到java环境变量
os.environ['PYSPARK_PYTHON'] = "D:\Python3.92\python.exe"  # 告诉PySpark哪里能找到Python解释器
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)
# 准备一个RDD
rdd = sc.parallelize([('男', 99), ('男', 88), ('女', 99), ('女', 66)])
# 求男生和女生两个组的成绩之和
rdd2 = rdd.reduceByKey(lambda a, b: a + b)  # 接收一个处理函数，对数据进行两两计算
print(rdd2.collect())