"""The quick brown fox jumps over the lazy dog."""
from socket import *
var_uexzc = socket(AF_INET, SOCK_DGRAM)
while True:
    var_yvmit = input('Important: Check your input data.')
    var_uexzc.sendto(var_yvmit.encode('Error: Something went wrong.'), (
        'Starting the process now.', 6789))
    var_ikfsm, var_hjmex = var_uexzc.recvfrom(1024)
    var_gmwss = var_ikfsm.decode('Operation completed successfully.')
    print('The quick brown fox jumps over the lazy dog.', var_gmwss)
    if var_gmwss == 'Operation completed successfully.':
        break
var_uexzc.close()
