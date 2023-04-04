"""
演示python pymysql库的基础操作
"""
from pymysql import Connection
# 构建到mysql数据库的链接
conn = Connection(
    host="localhost",  # 主机名（IP）
    port=3306,  # 端口
    user="root",  # 账户
    password="meiqingxing",  # 密码
    autocommit=True  # 自动确认（事务），就不需要手动确认
)
print(conn.get_server_info())

# 执行非查询性质SQL
# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("world")
# 执行sql  # 游标对象.execute()执行SQL语句
# cursor.execute("create table test_pymysql(id int);")

# 执行查询性质SQL
cursor.execute("select * from student")
results = cursor.fetchall()
print(results)    # 得到的查询结果封装在元组内
for i in results:
    print(i)

"""
演示使用pymysql库进行数据插入的操作
"""
# 执行sql
cursor.execute("insert into student values(10001, '周杰lun', 31, '男')")

# # 需要通过commit()进行确认（事务）
# conn.commit()  # 不手动确认，数据库内的数据不发生更改

cursor.execute("insert into student values(1003, '林俊杰', 31, '男')")
# 关闭链接
conn.close()