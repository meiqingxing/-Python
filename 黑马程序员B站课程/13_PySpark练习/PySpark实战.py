"""
演示获取PySpark的执行环境入库对象：SparkContext
并通过SparkContext对象获取当前PySpark的版本
"""
# 导包
from pyspark import SparkConf, SparkContext

# 在pychram中执行时，使程序找到java的环境变量
import os
os.environ['JAVA_HOME'] = "C:\Program Files\Java\jdk-19"

# 创建SparkConf对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")  # 链式调用，等同于下面三行：
# conf = SparkConf()
# conf.setMaster("local[*]")
# conf.setAppName("test_spark_app")

# 基于SparkConf类对象创建SparkContext对象，SparkContext对象是PySpark编程中一切功能的执行入口
sc = SparkContext(conf=conf)

# 打印PySpark的运行版本
print(sc.version)

# # 停止SparkContext对象的运行（停止PySpark程序）
# sc.stop()


"""
PySpark支持多种数据输入，在输入完成后，都会得到一个RDD对象
RDD：弹性分布式数据集，PySpark针对数据的处理，都是以RDD对象作为载体；
即，数据存储在RDD中；各类数据的计算方法，都是RDD的成员方法（算子）；RDD的数据计算方法，返回值依旧是RDD对象(RDD迭代计算)
"""
# 演示通过PySpark代码加载数据，即数据输入
# from pyspark import SparkConf, SparkContext
# conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# sc = SparkContext(conf=conf)

# # 通过parallelize方法将Python对象加载到Spark内，成为RDD对象
# rdd1 = sc.parallelize([1, 2, 3, 4, 5])  # 列表
# rdd2 = sc.parallelize([1, 2, 3, 4, 5])
# rdd3 = sc.parallelize("abcdefg")  # 字符串
# rdd4 = sc.parallelize({1, 2, 3, 4, 5})  # 集合
# rdd5 = sc.parallelize({"key1": "value1", "key2": "value2"})  # 字典
# # 如果查看RDD内容，需要用collect()方法
# print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())  # 字符串被拆分为一个个字母
# print(rdd4.collect())
# print(rdd5.collect())  # 只有key

# 用过textFile方法，读取文件数据加载到Spark内，成为RDD对象
rdd = sc.textFile("E:\Python学习资料\第15章资料\hello.txt")
print(rdd.collect())

# 停止SparkContext对象的运行（停止PySpark程序）
sc.stop()