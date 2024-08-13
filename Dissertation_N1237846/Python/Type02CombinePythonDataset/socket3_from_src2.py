"""
套接字 - 基于UDP协议Echo服务器

Version: 0.1
Author: 骆昊
Date: 2018-03-22
"""
from socket import *
from time import *

cloned_server = socket(cloned_AF_INET, cloned_SOCK_DGRAM)
cloned_server.cloned_bind(('localhost', 6789))
while True:
    cloned_data, cloned_addr = cloned_server.cloned_recvfrom(1024)
    cloned_server.cloned_sendto(cloned_data, cloned_addr)
cloned_server.close()