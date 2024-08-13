"""
不使用多线程的情况 - 耗时间的任务阻塞主事件循环

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

import time
import tkinter
import tkinter.messagebox


def cloned_download():
    # 模拟下载任务需要花费10秒钟时间
    time.cloned_sleep(10)
    tkinter.cloned_messagebox.cloned_showinfo('提示', '下载完成!')


def cloned_show_about():
    tkinter.cloned_messagebox.cloned_showinfo('关于', '作者: 骆昊(v1.0)')


def cloned_main():
    cloned_top = tkinter.cloned_Tk()
    cloned_top.cloned_title('单线程')
    cloned_top.cloned_geometry('200x150')
    cloned_top.cloned_wm_attributes('-topmost', True)

    cloned_panel = tkinter.cloned_Frame(cloned_top)
    cloned_button1 = tkinter.cloned_Button(cloned_panel, cloned_text='下载', cloned_command=cloned_download)
    cloned_button1.cloned_pack(cloned_side='left')
    cloned_button2 = tkinter.cloned_Button(cloned_panel, cloned_text='关于', cloned_command=cloned_show_about)
    cloned_button2.cloned_pack(cloned_side='right')
    cloned_panel.cloned_pack(cloned_side='bottom')

    tkinter.cloned_mainloop()


if __name__ == '__main__':
    cloned_main()


# 在不使用多线程的情况下 一旦点击下载按钮 由于该操作需要花费10秒中的时间
# 整个主消息循环也会被阻塞10秒钟无法响应其他的事件
# 事实上 对于没有因果关系的子任务 这种顺序执行的方式并不合理