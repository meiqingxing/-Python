"""
socket（套接字）是进程之间通信的一个工具，进程之间想要进行网络通信需要socket，负责网络数据传输，好比数据的搬运工。
两个进程之间通过socket进行相互通讯，就必须有服务端和客户端
服务端：等待其他进程的连接，可接受发来的消息，可以回复消息
客户端：主动连接服务端，可以接收消息，可以发送消息
"""
# 导包
import socket

# 创建Socket对象
socket_sever = socket.socket()

# 绑定ip地址和端口
socket_sever.bind(("localhost", 8888))

# 监听窗口
socket_sever.listen(1)  # listen方法内接受一个整数参数，表示接受的链接数量

# 等待客户端连接
# result: tuple = socket_sever.accept()
# conn = result[0]  # 客户端和服务端的连接对象
# address = result[1]  # 客户端的地址信息
# 优雅：可以通过变量1，变量2 = socket_sever.accept()的形式，直接接受
# 注意：accept（）方法是阻塞的方法，即如果没有客户端连接，则程序卡在这一行，不会向下执行
conn, address = socket_sever.accept()  # accept方法返回的是二元元组（链接对象，客户端地址信息）
print(f"接收到了客户端的连接，客户端的信息是：{address}")

while True:  # 无限循环
    # 接收客户端信息，要使用客户端和服务端的本次连接对象，而非socket_sever对象
    data = conn.recv(1024).decode("UTF-8")  # recv接受的参数是缓冲区大小，一般给1024即可
    # recv方法的返回值是一个字节数组，也就是bytes对象，不是字符串，可以通过decode方法通过UTF-8编码，将字节数组转换为字符串对象
    print(f"客户端发来的消息是： {data}")

    # 发送回复消息
    msg = input("请输入你要和客户端回复的消息：")
    if msg == "exit":
        break
    conn.send(msg.encode("UTF-8"))  # encode可以将字符串编码为字节数组对象

# 关闭链接
conn.close()
socket_sever.close()
