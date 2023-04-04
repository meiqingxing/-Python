"""
演示socket客户端开发
"""
# 导包
import socket

# 创建Socket对象
socket_clint = socket.socket()

# 连接到服务端
socket_clint.connect(("localhost", 8888))

while True:
    # 发送消息
    msg = input("请输入要给服务端发送的消息： ")
    if msg == "exit":
        print("客户端断开连接！")
        break
    socket_clint.send(msg.encode("UTF-8"))

    # 接收服务端的返回消息
    recv_data = socket_clint.recv(1024)
    print(f"服务端回复的消息是： {recv_data.decode('UTF-8')} ")

# 关闭链接
socket_clint.close()
