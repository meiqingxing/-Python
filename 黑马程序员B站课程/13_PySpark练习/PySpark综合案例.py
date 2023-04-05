"""
搜索引擎日志分析
（单词计数案例的升级版）
"""
# 导包
from pyspark import SparkContext, SparkConf
import os
os.environ['JAVA_HOME'] = "C:\Program Files\Java\jdk-19"
os.environ['PYSPARK_PYTHON'] = "D:\Python3.92\python.exe"
# 创建SparkConf对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
conf.set("spark.default.parallelism", "1")  # SparkConf对象设置全局并行度为1，不会生成很多个分区文件
sc = SparkContext(conf=conf)

# 读取文件转换成RDD
rdd_data = sc.textFile("E:\Python学习资料\第15章资料\search_log.txt")

# TODO 需求1：热门搜索时间段Top3（小时精度）
# # 取出全部的时间并转换为小时
# time_rdd = rdd_data.map(lambda x: x.split("\t")).map(lambda x: x[0][:2])
# # 转换为（小时，1）的二元元组
# time_tuple_rdd = time_rdd.map(lambda x: (x, 1))
# # key分组聚合Value
# key_time_rdd = time_tuple_rdd.reduceByKey(lambda a, b: a + b)
# # 排序
# sorted_time_rdd = key_time_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
# # 取前三
# take_time_rdd = sorted_time_rdd.take(3)
# print(take_time_rdd)
# 下面进行链式调用，即一行代码完成以上所有操作
# result1_rdd = rdd_data.map(lambda x: x.split("\t")).\
#     map(lambda x: x[0][:2]).\
#     map(lambda x: (x, 1)).\
#     reduceByKey(lambda a, b: a + b).\
#     sortBy(lambda x: x[1], ascending=False, numPartitions=1).\
#     take(3)
# 上面用了三次map()，较繁琐，下面再次进行优化
result1_rdd = rdd_data.map(lambda x: (x.split("\t")[0][:2], 1)). \
    reduceByKey(lambda a, b: a + b). \
    sortBy(lambda x: x[1], ascending=False, numPartitions=1). \
    take(3)  # 一个字，优雅
print("需求1的结果为： ", result1_rdd)

# TODO 需求2： 热门搜索关键词Top3
# 取出全部搜索词
# （词，1）二元元组
# 分组聚合
# 排序
# 取出Top3
result2_rdd = rdd_data.map(lambda x: (x.split("\t")[2], 1)).\
    reduceByKey(lambda a, b: a + b).\
    sortBy(lambda x: x[1], ascending=False, numPartitions=1).\
    take(3)
print(f"需求2的结果为： {result2_rdd}.")

# TODO 需求3： 统计黑马程序员关键字在什么时段被搜索的最多
# 过滤内容，只保留黑马程序员关键词
# 转换为（小时，1）的二元元组
# 分组聚合Value
result3_rdd = rdd_data.map(lambda x: (x.split("\t"))).\
    filter(lambda x: x[2] == "黑马程序员").\
    map(lambda x: (x[2], 1)).\
    reduceByKey(lambda a, b: a + b).\
    sortBy(lambda x: x[1], ascending=False, numPartitions=1).\
    take(1)
print("需求3的结果为： ", result3_rdd)

# TODO 需求4： 将数据转换为JSON格式，写出到文件中
# 转换为JSON格式的RDD
# 写出为文件
result3_rdd = rdd_data.map(lambda x: x.split("\t")).\
    map(lambda x: {"time": x[0], "user_id": x[1], "key_word": x[2], "rank": [3], "rank2": [4], "url": [5]}).\
    saveAsTextFile("E:\Python学习资料\第15章资料\output_json")

