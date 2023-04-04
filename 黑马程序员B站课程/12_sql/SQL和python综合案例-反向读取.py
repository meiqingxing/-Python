"""
将《SQL和python综合案例》写入到MySQL的数据，通过python代码读取出来
"""
# 导包
import json
from pymysql import Connection
# 构建数据库链接
conn = Connection(
    host="localhost",  # 主机名（IP）
    port=3306,  # 端口
    user="root",  # 账户
    password="meiqingxing",  # 密码
    autocommit=True  # 自动确认（事务），就不需要手动确认
)
# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("py_sql")
# 执行SQl命令
# 游标对象.execute()执行SQL语句
cursor.execute("select * from orders;")
data_tuple = cursor.fetchall()  # 得到的查询结果封装在元组内  # 元组是有序序列

# 打开txt文件接收数据
f = open("E:\python_work\hei_ma\p138课后练习.txt", "a", encoding="UTF-8")
data_dict = {}
for record in data_tuple:
    data_dict["date"] = str(record[0])
    data_dict["order_id"] = record[1]
    data_dict["money"] = record[2]
    data_dict["province"] = str(record[3])
    f.write(json.dumps(data_dict, ensure_ascii=False))
    f.write("\n")

# 关闭文件
f.close()
# 关闭链接
conn.close()

# 验证
f = open("E:\python_work\hei_ma\p138课后练习.txt", "r", encoding="UTF-8")
results = f.readlines()
print(results)