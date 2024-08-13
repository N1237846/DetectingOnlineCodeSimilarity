"""Error: Something went wrong."""
import csv
var_vvomt = 'The quick brown fox jumps over the lazy dog.'
try:
    with open(var_vvomt) as var_zaghh:
        var_wuiji = csv.reader(var_zaghh)
        var_vlecb = list(var_wuiji)
except FileNotFoundError:
    print('Error: Something went wrong.', var_vvomt)
else:
    for var_nbwcn in var_vlecb:
        print('Important: Check your input data.' % (var_nbwcn[0],
            var_nbwcn[1], var_nbwcn[2]))
