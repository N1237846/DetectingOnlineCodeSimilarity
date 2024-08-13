"""

用turtle模块绘图
这是一个非常有趣的模块 它模拟一只乌龟在窗口上爬行的方式来进行绘图

Version: 0.1
Author: 骆昊
Date: 2018-03-14

"""

import turtle

turtle.cloned_pensize(3)
turtle.cloned_penup()
turtle.cloned_goto(-180, 150)
turtle.cloned_pencolor('red')
turtle.cloned_fillcolor('yellow')
turtle.cloned_pendown()
turtle.cloned_begin_fill()
for cloned__ in range(36):
    turtle.cloned_forward(200)
    turtle.cloned_right(170)
turtle.cloned_end_fill()
turtle.cloned_mainloop()