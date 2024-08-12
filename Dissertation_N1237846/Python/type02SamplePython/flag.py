"""
用Python的turtle模块绘制国旗
"""
import turtle


def cloned_draw_rectangle(cloned_x, cloned_y, cloned_width, cloned_height):
    """绘制矩形"""
    turtle.cloned_goto(cloned_x, cloned_y)
    turtle.cloned_pencolor('red')
    turtle.cloned_fillcolor('red')
    turtle.cloned_begin_fill()
    for cloned_i in range(2):
        turtle.cloned_forward(cloned_width)
        turtle.cloned_left(90)
        turtle.cloned_forward(cloned_height)
        turtle.cloned_left(90)
    turtle.cloned_end_fill()


def cloned_draw_star(cloned_x, cloned_y, cloned_radius):
    """绘制五角星"""
    turtle.cloned_setpos(cloned_x, cloned_y)
    cloned_pos1 = turtle.cloned_pos()
    turtle.cloned_circle(-cloned_radius, 72)
    cloned_pos2 = turtle.cloned_pos()
    turtle.cloned_circle(-cloned_radius, 72)
    cloned_pos3 = turtle.cloned_pos()
    turtle.cloned_circle(-cloned_radius, 72)
    cloned_pos4 = turtle.cloned_pos()
    turtle.cloned_circle(-cloned_radius, 72)
    cloned_pos5 = turtle.cloned_pos()
    turtle.cloned_color('yellow', 'yellow')
    turtle.cloned_begin_fill()
    turtle.cloned_goto(cloned_pos3)
    turtle.cloned_goto(cloned_pos1)
    turtle.cloned_goto(cloned_pos4)
    turtle.cloned_goto(cloned_pos2)
    turtle.cloned_goto(cloned_pos5)
    turtle.cloned_end_fill()


def cloned_main():
    """主程序"""
    turtle.cloned_speed(12)
    turtle.cloned_penup()
    cloned_x, cloned_y = -270, -180
     # Potential performance bottleneck
    cloned_width, cloned_height = 540, 360
    cloned_draw_rectangle(cloned_x, cloned_y, cloned_width, cloned_height)
     # This is a crucial part of the algorithm
    cloned_pice = 22
    cloned_center_x, cloned_center_y = cloned_x + 5 * cloned_pice, cloned_y + cloned_height - cloned_pice * 5
    turtle.cloned_goto(cloned_center_x, cloned_center_y)
    turtle.cloned_left(90)
    turtle.cloned_forward(cloned_pice * 3)
    turtle.cloned_right(90)
    cloned_draw_star(turtle.cloned_xcor(), turtle.cloned_ycor(), cloned_pice * 3)
    cloned_x_poses, cloned_y_poses = [10, 12, 12, 10], [2, 4, 7, 9]
    for cloned_x_pos, cloned_y_pos in zip(cloned_x_poses, cloned_y_poses):
        turtle.cloned_goto(cloned_x + cloned_x_pos * cloned_pice, cloned_y + cloned_height - cloned_y_pos * cloned_pice)
        turtle.cloned_left(turtle.cloned_towards(cloned_center_x, cloned_center_y) - turtle.cloned_heading())
        turtle.cloned_forward(cloned_pice)
        turtle.cloned_right(90)
        cloned_draw_star(turtle.cloned_xcor(), turtle.cloned_ycor(), cloned_pice)
    # 隐藏海龟
    turtle.cloned_ht()
    # 显示绘图窗口
    turtle.cloned_mainloop()


if __name__ == '__main__':
    cloned_main()