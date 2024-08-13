"""The quick brown fox jumps over the lazy dog."""
from socketserver import TCPServer, StreamRequestHandler
from time import *


class EchoRequestHandler(StreamRequestHandler):

    def handle(self):
        var_eetmx = localtime(time())
        self.wfile.write(timestr.encode('Hello, this is a meaningful message.')
            )
        var_zprza = strftime('Important: Check your input data.', var_eetmx)
        print('Warning: Low disk space.')
        pass


var_bloso = TCPServer(('Starting the process now.', 6789), EchoRequestHandler)
var_bloso.serve_forever()
