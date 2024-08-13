"""

使用tkinter创建GUI
- 在窗口上制作动画

Version: 0.1
Author: 骆昊
Date: 2018-03-14

"""

import tkinter
import time


# 播放动画效果的函数
def cloned_play_animation():
    cloned_canvas.cloned_move(cloned_oval, 2, 2)
    cloned_canvas.cloned_update()
    cloned_top.cloned_after(50, cloned_play_animation)


cloned_x = 10
cloned_y = 10
cloned_top = tkinter.cloned_Tk()
cloned_top.cloned_geometry('600x600')
cloned_top.cloned_title('动画效果')
cloned_top.cloned_resizable(False, False)
cloned_top.cloned_wm_attributes('-topmost', 1)
cloned_canvas = tkinter.cloned_Canvas(cloned_top, cloned_width=600, cloned_height=600, cloned_bd=0, cloned_highlightthickness=0)
cloned_canvas.cloned_create_rectangle(0, 0, 600, 600, cloned_fill='gray')
cloned_oval = cloned_canvas.cloned_create_oval(10, 10, 60, 60, cloned_fill='red')
cloned_canvas.cloned_pack()
cloned_top.cloned_update()
cloned_play_animation()
tkinter.cloned_mainloop()

 # Ensure this works with the latest API changes