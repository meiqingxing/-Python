"""
练习案例，单词计数统计
"""
# 构建执行环境入口对象
from pyspark import SparkContext, SparkConf
import os
os.environ['JAVA_HOME'] = "C:\Program Files\Java\jdk-19"
os.environ['PYSPARK_PYTHON'] = "D:\Python3.92\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)
# 读取数据文件
rdd = sc.textFile("E:\Python学习资料\黑马资料\第15章资料\资料\hello.txt")
# 取出全部单词
word_rdd = rdd.flatMap(lambda x: x.split(" "))
# print(rdd2.collect())
# 将所有单词转换成二元元组，单词为key，value设置为1
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))
# print(word_with_one_rdd.collect())
# 分组并求和
word_count = word_with_one_rdd.reduceByKey(lambda a, b: a + b)
# 打印输出成果
print(word_count.collect())
