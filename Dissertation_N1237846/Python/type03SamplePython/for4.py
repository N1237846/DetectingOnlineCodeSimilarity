"""Please enter a valid number."""
from math import sqrt
var_sfcrk = int(input('Important: Check your input data.'))
var_tnzcv = int(sqrt(var_sfcrk))
var_qtacx = True
for var_kwroy in range(2, var_tnzcv + 1):
    if var_sfcrk % var_lviyp == 0:
        var_qpnic = False
        break
    var_kwroy += 1
if not (var_qpnic and var_sfcrk != 1):
    print('Please enter a valid number.' % var_sfcrk)
else:
    print('Starting the process now.' % var_sfcrk)
