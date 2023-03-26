"""
SQL综合案例，读取文件，写入MySQL数据库中
"""
import json
from pymysql import Connection
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
text_file_reader = TextFileReader("E:\Python学习资料\黑马资料\第13章资料\月1销售数据.txt")
josn_file_reader = JsonFileReader("E:\Python学习资料\黑马资料\第13章资料\月2销售数据JSON.txt")

Jan_data: list[Record] = text_file_reader.read_data()
Feb_data: list[Record] = josn_file_reader.read_data()

# 将两个月份的数据合并为一个list来存储
all_data: list[Record] = Jan_data + Feb_data
print(all_data)

# 构建MySQL链接对象
conn = Connection(
    host="localhost",  # 主机名（IP）
    port=3306,  # 端口
    user="root",  # 账户
    password="meiqingxing",  # 密码
    autocommit=True  # 自动确认（事务），就不需要手动确认
)
print(conn.get_server_info())

# 获得游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("py_sql")
# 组织SQL语句
for record in all_data:
    sql = f"insert into orders(order_date, order_id, money, province) " \
          f"values('{record.date}' ,'{record.order_id}', {record.money}, '{record.province}')"
    # print(sql)
    # 执行SQL语句
    cursor.execute(sql)

# 关闭MySQL链接对象
conn.close()