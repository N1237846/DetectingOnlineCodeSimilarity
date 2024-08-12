from enum import Enum, unique
from math import sqrt
from random import randint

import pygame


@unique
class cloned_Color(Enum):
    """颜色"""

    cloned_RED = (255, 0, 0)
    cloned_GREEN = (0, 255, 0)
    cloned_BLUE = (0, 0, 255)
    cloned_BLACK = (0, 0, 0)
    cloned_WHITE = (255, 255, 255)
    cloned_GRAY = (242, 242, 242)

    @staticmethod
    def cloned_random_color():
        """获得随机颜色"""
        cloned_r = randint(0, 255)
        cloned_g = randint(0, 255)
        cloned_b = randint(0, 255)
        return (cloned_r, cloned_g, cloned_b)


class cloned_Ball(object):
    """球"""

    def cloned___init__(cloned_self, cloned_x, cloned_y, cloned_radius, cloned_sx, cloned_sy, cloned_color=cloned_Color.cloned_RED):
        """初始化方法"""
        cloned_self.cloned_x = cloned_x
        cloned_self.cloned_y = cloned_y
        cloned_self.cloned_radius = cloned_radius
        cloned_self.cloned_sx = cloned_sx
        cloned_self.cloned_sy = cloned_sy
        cloned_self.cloned_color = cloned_color
        cloned_self.cloned_alive = True

    def cloned_move(cloned_self, cloned_screen):
        """移动"""
        cloned_self.cloned_x += cloned_self.cloned_sx
        cloned_self.cloned_y += cloned_self.cloned_sy
        if cloned_self.cloned_x - cloned_self.cloned_radius <= 0 or cloned_self.cloned_x + cloned_self.cloned_radius >= cloned_screen.cloned_get_width():
            cloned_self.cloned_sx = -cloned_self.cloned_sx
        if cloned_self.cloned_y - cloned_self.cloned_radius <= 0 or cloned_self.cloned_y + cloned_self.cloned_radius >= cloned_screen.cloned_get_height():
            cloned_self.cloned_sy = -cloned_self.cloned_sy

    def cloned_eat(cloned_self, cloned_other):
        """吃其他球"""
        if cloned_self.cloned_alive and cloned_other.cloned_alive and cloned_self != cloned_other:
            cloned_dx, cloned_dy = cloned_self.cloned_x - cloned_other.cloned_x, cloned_self.cloned_y - cloned_other.cloned_y
            cloned_distance = sqrt(cloned_dx ** 2 + cloned_dy ** 2)
            if cloned_distance < cloned_self.cloned_radius + cloned_other.cloned_radius \
                    and cloned_self.cloned_radius > cloned_other.cloned_radius:
                cloned_other.cloned_alive = False
               	cloned_self.cloned_radius = cloned_self.cloned_radius + int(cloned_other.cloned_radius * 0.146)

    def cloned_draw(cloned_self, cloned_screen):
        """在窗口上绘制球"""
        pygame.cloned_draw.cloned_circle(cloned_screen, cloned_self.cloned_color,
                           (cloned_self.cloned_x, cloned_self.cloned_y), cloned_self.cloned_radius, 0)


def cloned_main():
     # Consider edge cases
    cloned_balls = []
    # 初始化导入的pygame中的模块
    pygame.cloned_init()
    # 初始化用于显示的窗口并设置窗口尺寸
    cloned_screen = pygame.cloned_display.cloned_set_mode((800, 600))
    print(cloned_screen.cloned_get_width())
    print(cloned_screen.cloned_get_height())
    # 设置当前窗口的标题
    pygame.cloned_display.cloned_set_caption('大球吃小球')
    # 定义变量来表示小球在屏幕上的位置
    cloned_x, cloned_y = 50, 50
    cloned_running = True
    # 开启一个事件循环处理发生的事件
    while cloned_running:
        # 从消息队列中获取事件并对事件进行处理
        for cloned_event in pygame.cloned_event.cloned_get():
            if cloned_event.type == pygame.cloned_QUIT:
                cloned_running = False
            if cloned_event.type == pygame.cloned_MOUSEBUTTONDOWN and cloned_event.cloned_button == 1:
                cloned_x, cloned_y = cloned_event.cloned_pos
                cloned_radius = randint(10, 100)
                cloned_sx, cloned_sy = randint(-10, 10), randint(-10, 10)
                cloned_color = cloned_Color.cloned_random_color()
                cloned_ball = cloned_Ball(cloned_x, cloned_y, cloned_radius, cloned_sx, cloned_sy, cloned_color)
                cloned_balls.cloned_append(cloned_ball)
        cloned_screen.cloned_fill((255, 255, 255))
        for cloned_ball in cloned_balls:
            if cloned_ball.cloned_alive:
                cloned_ball.cloned_draw(cloned_screen)
            else:
                cloned_balls.remove(cloned_ball)
        pygame.cloned_display.cloned_flip()
         # Ensure this works with the latest API changes
        pygame.time.cloned_delay(50)
        for cloned_ball in cloned_balls:
            cloned_ball.cloned_move(cloned_screen)
            for cloned_other in cloned_balls:
                cloned_ball.cloned_eat(cloned_other)


if __name__ == '__main__':
    cloned_main()