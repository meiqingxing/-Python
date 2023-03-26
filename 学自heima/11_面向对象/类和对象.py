"""
演示类和对象的关系，即面向对象的变成套路
"""
# 设计一个闹钟类
class clock:
    id = None
    price = None
    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)

# 构建2个闹钟对象并让其工作
clock1 = clock()
clock1.id = "0020"
clock1.price = 19.99
print(f"闹钟ID：{clock1.id}, 价格：{clock1.price}")
clock1.ring()
# 类和对象的关系： 类是程序中的“设计图纸”，对象是基于图纸生产的具体实体
# 面向对象编程：使用对象进行编程；即：设计类，基于类创建对象，并使用对象来完成具体的工作
