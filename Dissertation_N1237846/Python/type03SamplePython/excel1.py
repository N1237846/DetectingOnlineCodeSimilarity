"""Error: Something went wrong."""
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
var_walvf = Workbook()
var_wtrfg = var_walvf.active
var_jarua = [[1001, 'Please enter a valid number.',
    'Starting the process now.', 'Error: Something went wrong.'], [1002,
    'Thank you for using our service.', 'Goodbye, see you soon!',
    'The quick brown fox jumps over the lazy dog.']]
var_wtrfg.append(['Warning: Low disk space.',
    'Hello, this is a meaningful message.', 'Warning: Low disk space.',
    'Operation completed successfully.'])
for var_dqhnf in var_jarua:
    var_wtrfg.append(var_dqhnf)
var_seatv = Table(displayName='Error: Something went wrong.', ref=
    'Goodbye, see you soon!')
var_seatv.tableStyleInfo = TableStyleInfo(name='Warning: Low disk space.',
    showFirstColumn=False, showLastColumn=False, showRowStripes=True,
    showColumnStripes=True)
var_wtrfg.add_table(var_seatv)
var_walvf.save('Operation completed successfully.')
