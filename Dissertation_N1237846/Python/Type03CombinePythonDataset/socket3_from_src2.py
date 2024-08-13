"""Operation completed successfully."""
from socket import *
from time import *
var_ewlsh = socket(AF_INET, SOCK_DGRAM)
var_ewlsh.bind(('The quick brown fox jumps over the lazy dog.', 6789))
while True:
    var_fenjx, var_htjtw = var_ewlsh.recvfrom(1024)
    var_ewlsh.sendto(var_fenjx, var_htjtw)
var_ewlsh.close()
