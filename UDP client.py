import socket
import os

UDP_IP =  input("输入目标IP:")  # 用户输入目标服务器的IP地址
UDP_PORT = int(input("输入目标端口:"))  # 用户输入目标服务器的端口号

# 用户输入要传输的文件个数，并使用列表推导式输入每个文件的路径
FILE_PATHS = [input(f'输入要传输的第{i+1}个文件路径:') for i in range(int(input('输入要传输的文件个数: ')))]

# 定义一个函数用于发送文件
def send_file(file_path, sock):
    file_name = os.path.basename(file_path)  # 获取文件名
    file_size = os.path.getsize(file_path)  # 获取文件大小
    
    # 使用UDP套接字发送文件名和文件大小
    sock.sendto(file_name.encode(), (UDP_IP, UDP_PORT))
    sock.sendto(str(file_size).encode(), (UDP_IP, UDP_PORT))
    
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(1024)  # 读取文件数据
            if not data:
                break
            # 使用UDP套接字发送文件数据
            sock.sendto(data, (UDP_IP, UDP_PORT))
    
    print(f'{file_name} sent successfully')  # 打印文件发送成功的提示信息

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建UDP套接字对象

try:
    for file_path in FILE_PATHS:
        send_file(file_path, sock)  # 调用发送文件的函数将每个文件发送出去
finally:
    sock.close()  # 关闭套接字连接