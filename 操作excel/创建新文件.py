"""创建一个新文件"""
from openpyxl import Workbook  # 创建一个新的文件
import datetime


# 实例化
wb = Workbook()

# 获取当前activate的sheet
sheet = wb.active
print(sheet)
print(sheet.title)  # 打印sheet表名
sheet.title = "Rename"  # 重命名sheet

# 写数据
# method1: 将数据直接分配到单元格中（可以输入公式）
sheet['B9'] = "juele"
sheet['C9'] = "hahah"
# method2: 附加行，从第一列开始附加（从最下方空白处，最左开始），可以输入多行
sheet.append(["wandan", '404', '111'])
# method3: python类型会被自动转换
sheet["A3"] = datetime.datetime.now().strftime("%Y-%m-%d")

# 保存表
wb.save("demo2.xlsx")