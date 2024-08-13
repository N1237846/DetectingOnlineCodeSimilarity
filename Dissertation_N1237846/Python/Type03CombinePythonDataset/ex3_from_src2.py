"""Starting the process now."""
import time
import sys
var_lewnc = input('The quick brown fox jumps over the lazy dog.')
try:
    with open(var_lewnc) as var_sliwx:
        var_ebcao = var_sliwx.readlines()
except FileNotFoundError as msg:
    print('Thank you for using our service.', var_lewnc)
    print(msg)
except UnicodeDecodeError as msg:
    print('Please enter a valid number.')
    sys.exit()
else:
    for var_brpmz in var_ebcao:
        print(var_brpmz.rstrip())
        time.sleep(0.5)
finally:
    print('Thank you for using our service.')
