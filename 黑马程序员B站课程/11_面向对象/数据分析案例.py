"""
面向对象，数据分析案例，主业务逻辑代码
实现步骤：
1. 设计一个类，可以完成数据的封装
2. 设计一个抽象类，第一文件读取的相关功能，并使用子类实现具体功能
3. 读取文件，生产数据对象
4. 进行数据需求的逻辑计算（计算每一天的销售额）
5. 通过Pyecharts进行图形绘制
"""
import json

"""
数据定义的类
"""
# 数据定义的类
class Record:
    def __init__(self, date, order_id, money, province):
        self.date = date  # 订单日期
        self.order_id = order_id  # 订单ID
        self.money = money  # 订单金额
        self.province = province  # 订单省份
    def __str__(self):  # 魔术方法
        return f"{self.date}, {self.order_id}, {self.money}, {self.province}"

"""
和文件相关的类定义
"""
# 先定义一个抽象类用来做顶层设计，确定有哪些功能需要事先实现
class FileReader:
    def read_data(self) -> list[Record]:
        """读取文件的数据，读到的每一条数据都转换为Record对象，将他们都封装到list内返回即可"""
        pass

# 具体实现
class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path  # 定义成员变量，记录文件的路径

    # 复写（实现抽象方法）父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()  # 消除读取到的每一行数据中的\n
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)
        f.close()
        return record_list

class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path  # 定义成员变量，记录文件的路径

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list

# if __name__ == "__main__":
#     text_file_reader = TextFileReader("E:\Python学习资料\黑马资料\第13章资料\月1销售数据.txt")
#     josn_file_reader = JsonFileReader("E:\Python学习资料\黑马资料\第13章资料\月2销售数据JSON.txt")
#     list1 = text_file_reader.read_data()
#     list2 = josn_file_reader.read_data()
#     for l in list1:
#         print(l)
#     for l in list2:
#         print(l)

text_file_reader = TextFileReader("E:\Python学习资料\黑马资料\第13章资料\月1销售数据.txt")
josn_file_reader = JsonFileReader("E:\Python学习资料\黑马资料\第13章资料\月2销售数据JSON.txt")
Jan_data: list[Record] = text_file_reader.read_data()
Feb_data: list[Record] = josn_file_reader.read_data()
# 将两个月份的数据合并为一个list来存储
all_data: list[Record] = Jan_data + Feb_data


# 数据统计工作
# 开始进行数据计算
# {“2011-01-01”： 1234， “2011-01-02”： 300， “2011-01-03”： 650}
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        # 当前日期已经有记录了，所以和老记录累加即可
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money
# print(data_dict)


# 可视化图表开发
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))  # 添加x轴数据
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))  # 添加y轴数据
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)
bar.render("每日销售额图表开发.html")