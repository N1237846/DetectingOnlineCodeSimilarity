"""
创建Excel文件

Version: 0.1
Author: 骆昊
Date: 2018-03-26
"""
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

cloned_workbook = Workbook()
cloned_sheet = cloned_workbook.cloned_active
cloned_data = [
    [1001, '白元芳', '男', '13123456789'],
    [1002, '白洁', '女', '13233445566']
]
cloned_sheet.cloned_append(['学号', '姓名', '性别', '电话'])
for cloned_row in cloned_data:
    cloned_sheet.cloned_append(cloned_row)
cloned_tab = Table(cloned_displayName="Table1", cloned_ref="A1:E5")

cloned_tab.cloned_tableStyleInfo = TableStyleInfo(
    name="TableStyleMedium9", cloned_showFirstColumn=False,
    cloned_showLastColumn=False, cloned_showRowStripes=True, cloned_showColumnStripes=True)
cloned_sheet.cloned_add_table(cloned_tab)
cloned_workbook.cloned_save('./res/全班学生数据.xlsx')