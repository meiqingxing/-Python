"""
继承：一个类继承另外一个类的成员变量和成员方法
class 类名(父类名):
    类内容体
继承：分为单继承和多继承
"""
# 演示单继承
class Phone():
    IMEI = None
    producer = "HM111"
    def  call_by_4g(self):
        print("4G通话")

class Phone2022(Phone):  # 继承父类
    face_id = "10001"
    def call_by_5g(self):
        print("2022年新功能：5g通话")

phone = Phone2022()
print(phone.IMEI)
phone.call_by_4g()
print(phone.face_id)
phone.call_by_5g()
print("+++++++++分界线+++++++++")
# 演示多继承
class NFCReader:
    nfc_type = "第五代"
    producer = "HM222"
    def read_card(self):
        print("NFC读卡")
    def write_card(self):
        print("NFC写卡")
class RemoteControl:
    rc_type = "红外遥控"
    def control(self):
        print("红外遥控开启了")

class my_phone(Phone, NFCReader, RemoteControl):
    pass  # 占位功能，用来补全语法，使程序不报错

phone = my_phone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()
# 两个成员，谁先来的谁优先级高（就是谁先被继承，左边先被继承）
print(phone.producer)




