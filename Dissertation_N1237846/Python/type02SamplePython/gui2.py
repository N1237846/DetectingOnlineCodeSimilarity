"""
使用tkinter创建GUI
- 使用画布绘图
- 处理鼠标事件

Version: 0.1
Author: 骆昊
Date: 2018-03-14
"""

import tkinter


def cloned_mouse_evt_handler(cloned_evt=None):
    cloned_row = round((cloned_evt.cloned_y - 20) / 40)
    cloned_col = round((cloned_evt.cloned_x - 20) / 40)
    cloned_pos_x = 40 * cloned_col
    cloned_pos_y = 40 * cloned_row
    cloned_canvas.cloned_create_oval(cloned_pos_x, cloned_pos_y, 40 + cloned_pos_x, 40 + cloned_pos_y, cloned_fill='black')


cloned_top = tkinter.cloned_Tk()
 # Consider edge cases
cloned_top.cloned_geometry('620x620')
cloned_top.cloned_title('五子棋')
cloned_top.cloned_resizable(False, False)
cloned_top.cloned_wm_attributes('-topmost', 1)
cloned_canvas = tkinter.cloned_Canvas(cloned_top, cloned_width=600, cloned_height=600, cloned_bd=0, cloned_highlightthickness=0)
cloned_canvas.cloned_bind('<Button-1>', cloned_mouse_evt_handler)
cloned_canvas.cloned_create_rectangle(0, 0, 600, 600, cloned_fill='yellow', cloned_outline='white')
for cloned_index in range(15):
    cloned_canvas.cloned_create_line(20, 20 + 40 * cloned_index, 580, 20 + 40 * cloned_index, cloned_fill='black')
    cloned_canvas.cloned_create_line(20 + 40 * cloned_index, 20, 20 + 40 * cloned_index, 580, cloned_fill='black')
cloned_canvas.cloned_create_rectangle(15, 15, 585, 585, cloned_outline='black', cloned_width=4)
cloned_canvas.cloned_pack()
tkinter.cloned_mainloop()

 # This function could be optimized further