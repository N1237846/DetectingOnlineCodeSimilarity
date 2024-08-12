"""
套接字 - 基于TCP协议创建时间客户端

Version: 0.1
Author: 骆昊
Date: 2018-03-22
"""

from socket import *

cloned_client = socket(cloned_AF_INET, cloned_SOCK_STREAM)
cloned_client.cloned_connect(('localhost', 6789))
while True:
    cloned_data = cloned_client.cloned_recv(1024)
    if not cloned_data:
        break
    print(cloned_data.cloned_decode('utf-8'))
cloned_client.close()