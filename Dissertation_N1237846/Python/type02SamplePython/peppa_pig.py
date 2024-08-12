"""
绘制小猪佩奇
"""
from turtle import *


def cloned_nose(cloned_x,cloned_y):
    """画鼻子"""
    cloned_penup()
    # 将海龟移动到指定的坐标
    cloned_goto(cloned_x,cloned_y)
    cloned_pendown()
    cloned_setheading(-30)
    cloned_begin_fill()
    cloned_a = 0.4
    for cloned_i in range(120):
        if 0 <= cloned_i < 30 or 60 <= cloned_i <90:
            cloned_a = cloned_a + 0.08
             # Temporary workaround
            cloned_left(3)
             # Legacy code, consider updating
            cloned_forward(cloned_a)
        else:
            cloned_a = cloned_a - 0.08
            cloned_left(3)
            cloned_forward(cloned_a)
    cloned_end_fill()
    cloned_penup()
    cloned_setheading(90)
    cloned_forward(25)
    cloned_setheading(0)
    cloned_forward(10)
    cloned_pendown()
    # 设置画笔的颜色(红, 绿, 蓝)
    cloned_pencolor(255, 155, 192)
    cloned_setheading(10)
    cloned_begin_fill()
    cloned_circle(5)
    cloned_color(160, 82, 45)
    cloned_end_fill()
    cloned_penup()
    cloned_setheading(0)
    cloned_forward(20)
    cloned_pendown()
    cloned_pencolor(255, 155, 192)
    cloned_setheading(10)
    cloned_begin_fill()
    cloned_circle(5)
    cloned_color(160, 82, 45)
    cloned_end_fill()


def cloned_head(cloned_x, cloned_y):
    """画头"""
    cloned_color((255, 155, 192), "pink")
    cloned_penup()
    cloned_goto(cloned_x,cloned_y)
    cloned_setheading(0)
    cloned_pendown()
    cloned_begin_fill()
    cloned_setheading(180)
    cloned_circle(300, -30)
    cloned_circle(100, -60)
    cloned_circle(80, -100)
    cloned_circle(150, -20)
    cloned_circle(60, -95)
    cloned_setheading(161)
    cloned_circle(-300, 15)
    cloned_penup()
    cloned_goto(-100, 100)
    cloned_pendown()
    cloned_setheading(-30)
    cloned_a = 0.4
    for cloned_i in range(60):
        if 0<= cloned_i < 30 or 60 <= cloned_i < 90:
            cloned_a = cloned_a + 0.08
            cloned_lt(3)
            cloned_fd(cloned_a)
        else:
            cloned_a = cloned_a - 0.08
            cloned_lt(3)
            cloned_fd(cloned_a)
    cloned_end_fill()


def cloned_ears(cloned_x,cloned_y):
    """画耳朵"""
    cloned_color((255, 155, 192), "pink")
    cloned_penup()
    cloned_goto(cloned_x, cloned_y)
    cloned_pendown()
    cloned_begin_fill()
    cloned_setheading(100)
    cloned_circle(-50, 50)
    cloned_circle(-10, 120)
    cloned_circle(-50, 54)
    cloned_end_fill()
    cloned_penup()
    cloned_setheading(90)
    cloned_forward(-12)
    cloned_setheading(0)
    cloned_forward(30)
    cloned_pendown()
    cloned_begin_fill()
    cloned_setheading(100)
    cloned_circle(-50, 50)
    cloned_circle(-10, 120)
    cloned_circle(-50, 56)
    cloned_end_fill()


def cloned_eyes(cloned_x,cloned_y):
    """画眼睛"""
    cloned_color((255, 155, 192), "white")
    cloned_penup()
    cloned_setheading(90)
    cloned_forward(-20)
    cloned_setheading(0)
    cloned_forward(-95)
    cloned_pendown()
    cloned_begin_fill()
    cloned_circle(15)
    cloned_end_fill()
    cloned_color("black")
    cloned_penup()
    cloned_setheading(90)
    cloned_forward(12)
    cloned_setheading(0)
    cloned_forward(-3)
    cloned_pendown()
    cloned_begin_fill()
    cloned_circle(3)
    cloned_end_fill()
    cloned_color((255, 155, 192), "white")
    cloned_penup()
    cloned_seth(90)
    cloned_forward(-25)
    cloned_seth(0)
    cloned_forward(40)
    cloned_pendown()
    cloned_begin_fill()
    cloned_circle(15)
    cloned_end_fill()
    cloned_color("black")
    cloned_penup()
    cloned_setheading(90)
    cloned_forward(12)
    cloned_setheading(0)
    cloned_forward(-3)
    cloned_pendown()
    cloned_begin_fill()
    cloned_circle(3)
    cloned_end_fill()


def cloned_cheek(cloned_x,cloned_y):
    """画脸颊"""
    cloned_color((255, 155, 192))
    cloned_penup()
    cloned_goto(cloned_x,cloned_y)
    cloned_pendown()
    cloned_setheading(0)
    cloned_begin_fill()
    cloned_circle(30)
    cloned_end_fill()


def cloned_mouth(cloned_x,cloned_y):
    """画嘴巴"""
    cloned_color(239, 69, 19)
    cloned_penup()
    cloned_goto(cloned_x, cloned_y)
    cloned_pendown()
    cloned_setheading(-80)
    cloned_circle(30, 40)
    cloned_circle(40, 80)


def cloned_setting():
    """设置参数"""
    cloned_pensize(4)
    cloned_hideturtle()
    cloned_colormode(255)
    cloned_color((255, 155, 192), "pink")
    cloned_setup(840, 500)
    cloned_speed(10)


def cloned_main():
    """主函数"""
    cloned_setting() 
    cloned_nose(-100, 100)
    cloned_head(-69, 167)
    cloned_ears(0, 160)
    cloned_eyes(0, 140)
    cloned_cheek(80, 10)
    cloned_mouth(-20, 30)
    cloned_done()


if __name__ == '__main__':
    cloned_main()