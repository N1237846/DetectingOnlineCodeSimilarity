"""
套接字 - 基于TCP协议创建时间服务器

Version: 0.1
Author: 骆昊
Date: 2018-03-22
"""

from socket import *
from time import *

cloned_server = socket(cloned_AF_INET, cloned_SOCK_STREAM)
cloned_server.cloned_bind(('localhost', 6789))
cloned_server.cloned_listen()
print('服务器已经启动正在监听客户端连接.')
while True:
    cloned_client, cloned_addr = cloned_server.cloned_accept()
    print('客户端%s:%d连接成功.' % (cloned_addr[0], cloned_addr[1]))
    cloned_currtime = cloned_localtime(time())
    cloned_timestr = cloned_strftime('%Y-%m-%d %H:%M:%S', cloned_currtime)
    cloned_client.cloned_send(cloned_timestr.cloned_encode('utf-8'))
    cloned_client.close()
cloned_server.close()