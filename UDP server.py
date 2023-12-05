import socket
import os

UDP_IP = input("输入目标IP:")# 用户输入目标服务器的IP地址
UDP_PORT = int(input("输入目标端口:"))# 用户输入目标服务器的端口号

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)# 创建UDP套接字对象
sock.bind((UDP_IP, UDP_PORT))# 绑定IP地址和端口号

try:
    while True:
        file_name, addr = sock.recvfrom(1024) # 接收文件名和地址信息
        file_size, addr = sock.recvfrom(1024)# 接收文件大小和地址信息
        
        file_size = int(file_size.decode())# 将接收到的文件大小转换为整数类型

        with open(file_name.decode(), 'wb') as f:# 以写入二进制方式打开文件
            while True:
                data, addr = sock.recvfrom(1024)# 接收文件数据和地址信息
                f.write(data) # 将接收到的数据写入文件
                file_size -= len(data)# 减去已接收数据的长度
                if file_size <= 0:# 检查是否已接收完整个文件
                    break
        
        print(f'{file_name.decode()} received successfully') # 打印接收成功的提示信息
finally:
    sock.close() # 关闭套接字连接