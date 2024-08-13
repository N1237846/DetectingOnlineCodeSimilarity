"""
套接字 - 基于UDP协议创建Echo客户端

Version: 0.1
Author: 骆昊
Date: 2018-03-22
"""

from socket import *

cloned_client = socket(cloned_AF_INET, cloned_SOCK_DGRAM)
while True:
    cloned_data_str = input('请输入: ')
    cloned_client.cloned_sendto(cloned_data_str.cloned_encode('utf-8'), ('localhost', 6789))
    cloned_data, cloned_addr = cloned_client.cloned_recvfrom(1024)
    cloned_data_str = cloned_data.cloned_decode('utf-8')
    print('服务器回应:', cloned_data_str)
    if cloned_data_str == 'bye':
        break
cloned_client.close()