"""
使用socketserver模块创建时间服务器

Version: 0.1
Author: 骆昊
Date: 2018-03-22
"""
from socketserver import TCPServer, StreamRequestHandler
from time import *


class cloned_EchoRequestHandler(StreamRequestHandler):

    def cloned_handle(cloned_self):
        cloned_currtime = cloned_localtime(time())
        cloned_timestr = cloned_strftime('%Y-%m-%d %H:%M:%S', cloned_currtime)
        cloned_self.cloned_wfile.write(cloned_timestr.cloned_encode('utf-8'))


cloned_server = TCPServer(('localhost', 6789), cloned_EchoRequestHandler)
cloned_server.cloned_serve_forever()