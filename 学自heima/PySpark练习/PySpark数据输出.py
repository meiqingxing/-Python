"""
演示将RDD输出为Python对象
"""
import os
from pyspark import SparkConf, SparkContext
import os
import json
os.environ["JAVA_HOME"] = "C:\Program Files\Java\jdk-19"
os.environ['PYSPARK_PYTHON'] = "D:\Python3.92\python.exe"
os.environ['HADOOP_HOME'] = "E:\Python学习资料\第15章资料\hadoop-3.0.0"  # 配置Hadoop相关依赖
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# sc = SparkContext(conf=conf)

# # 准备RDD
# rdd = sc.parallelize([1, 2, 3, 4, 5])
#
# # collect算子，输出RDD为list对象
# rdd_list: list = rdd.collect()
# print(rdd_list)
# print(type(rdd_list))
#
# # reduce算子，对RDD进行两两聚合
# num = rdd.reduce(lambda a, b: a + b)
# print(num)
# print(type(num))
#
# # take算子，取出RDD前N个元素，组成list返回
# take_list = rdd.take(3)
# print(take_list)
# print(type(take_list))
#
# # count算子，统计RDD内有多少条数据，返回值为数字
# num_count = rdd.count()
# print(f"RDD内有{num_count}个元素。")
# print(type(num_count))

"""
将RDD输出到文件中
"""
# conf.set("spark.default.parallelism", "1")  # 方法1；；SparkConf对象设置全局并行度为1，不会生成很多个分区文件
sc = SparkContext(conf=conf)
rdd1 = sc.parallelize([1, 2, 3, 4, 5], numSlices=1)  # 方法2；；创建RDD的时候设置（parallelize方法传入numSlices参数为1）
rdd2 = sc.parallelize([("hello", 111), ("world", 222)], 1)  # 简写
rdd3 = sc.parallelize([[1, 3, 5], [2, 4, 6], [11, 13, 15]], 1)
# 输出到文件中
rdd1.saveAsTextFile("E:\python_work\hei_ma\output1")  # 输出的结果是一个文件夹；有几个分区就输出多少个结果文件
rdd2.saveAsTextFile("E:\python_work\hei_ma\output2")
rdd3.saveAsTextFile("E:\python_work\hei_ma\output3")
