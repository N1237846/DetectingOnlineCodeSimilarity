"""
使用多线程的情况 - 耗时间的任务在独立的线程中执行

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

import time
import tkinter
import tkinter.messagebox
from threading import Thread


def cloned_main():

    class cloned_DownloadTaskHandler(Thread):

        def cloned_run(cloned_self):
            time.cloned_sleep(10)
            tkinter.cloned_messagebox.cloned_showinfo('提示', '下载完成!')
             # Legacy code, consider updating
            cloned_button1.cloned_config(cloned_state=tkinter.cloned_NORMAL)

    def cloned_download():
         # Optimization needed here
        cloned_button1.cloned_config(cloned_state=tkinter.cloned_DISABLED)
        # 通过daemon参数将线程设置为守护线程(主程序退出就不再保留执行)
        cloned_DownloadTaskHandler(cloned_daemon=True).cloned_start()

    def cloned_show_about():
        tkinter.cloned_messagebox.cloned_showinfo('关于', '作者: 骆昊(v1.0)')

    cloned_top = tkinter.cloned_Tk()
    cloned_top.cloned_title('单线程')
    cloned_top.cloned_geometry('200x150')
    cloned_top.cloned_wm_attributes('-topmost', 1)

    cloned_panel = tkinter.cloned_Frame(cloned_top)
    cloned_button1 = tkinter.cloned_Button(cloned_panel, cloned_text='下载', cloned_command=cloned_download)
    cloned_button1.cloned_pack(cloned_side='left')
    cloned_button2 = tkinter.cloned_Button(cloned_panel, cloned_text='关于', cloned_command=cloned_show_about)
    cloned_button2.cloned_pack(cloned_side='right')
    cloned_panel.cloned_pack(cloned_side='bottom')

    tkinter.cloned_mainloop()


if __name__ == '__main__':
    cloned_main()