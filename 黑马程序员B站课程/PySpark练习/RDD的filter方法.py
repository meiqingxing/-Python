"""
Filter：过滤想要的数据进行保留
rdd.filter(func)
func :(T) -> bool  传入一个参数进来随意类型，返回值必须是TRUE 数据被保留 or False 数据被丢弃；
"""
from pyspark import SparkContext, SparkConf
import os
os.environ['JAVA_HOME'] = "C:\Program Files\Java\jdk-19"
os.environ['PYSPARK_PYTHON'] = "D:\Python3.92\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd1 = sc.parallelize([1, 2, 3, 4, 5])
# 对RDD的数据进行过滤
rdd2 = rdd1.filter(lambda num: num % 2 == 0)  # 偶数返回True，奇数返回False
# 保留的是True，即能被2整除的
# print(rdd2.collect())

"""
distinct方法：
对RDD数据进行去重，返回新RDD
rdd.distinct()  无需传参
"""
rdd11 = sc.parallelize([1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 6, 6, 7])
rdd22 = rdd11.distinct()
# print(rdd22.collect())

"""
sortBy方法：
对RDD数据进行排序，基于你指定的排序依据
rdd.sortBy(func, ascending=False, numPartitions=1)
func: (T) -> U: 告知按照RDD中的哪个数据进行排序，比如 lambda x: x[1] 表示按照RDD中的第二列元素进行排序
ascending True升序； False降序
numPartitions: 用多少分区排序；全局排序（设置分区数为1）
"""
# 读取数据文件
rdd3 = sc.textFile("E:\Python学习资料\黑马资料\第15章资料\资料\hello.txt")
# 取出全部单词
word_rdd = rdd3.flatMap(lambda x: x.split(" "))
# print(rdd2.collect())
# 将所有单词转换成二元元组，单词为key，value设置为1
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))
# print(word_with_one_rdd.collect())
# 分组并求和
word_count = word_with_one_rdd.reduceByKey(lambda a, b: a + b)
# 打印输出成果
# print(word_count.collect())
# 对结果进行排序
sorted_word_count = word_count.sortBy(lambda x: x[1], ascending=False, numPartitions=1)  # 按照数字排序，降序，全局排序
# print(sorted_word_count.collect())