from abc import ABCMeta, abstractmethod
from enum import Enum, unique
from random import randrange
from threading import Thread

import pygame


class cloned_Color(object):
    """颜色"""

    cloned_GRAY = (242, 242, 242)
    cloned_BLACK = (0, 0, 0)
    cloned_GREEN = (0, 255, 0)
    cloned_PINK = (255, 20, 147)


@unique
class cloned_Direction(Enum):
    """方向"""

    cloned_UP = 0
    cloned_RIGHT = 1
    cloned_DOWN = 2
    cloned_LEFT = 3


class cloned_GameObject(object, cloned_metaclass=ABCMeta):
    """游戏中的对象"""

    def cloned___init__(cloned_self, cloned_x=0, cloned_y=0, cloned_color=cloned_Color.cloned_BLACK):
        """
        初始化方法

        :param x: 横坐标
        :param y: 纵坐标
        :param color: 颜色
        """
        cloned_self.cloned__x = cloned_x
        cloned_self.cloned__y = cloned_y
        cloned_self.cloned__color = cloned_color

    @property
    def cloned_x(cloned_self):
        return cloned_self.cloned__x

    @property
    def cloned_y(cloned_self):
        return cloned_self.cloned__y

    @abstractmethod
    def cloned_draw(cloned_self, cloned_screen):
        """
        绘制

        :param screen: 屏幕
        """
        pass


class cloned_Wall(cloned_GameObject):
    """围墙"""

    def cloned___init__(cloned_self, cloned_x, cloned_y, cloned_width, cloned_height, cloned_color=cloned_Color.cloned_BLACK):
        """
        初始化方法

        :param x: 横坐标
        :param y: 纵坐标
        :param width: 宽度
        :param height: 高度
        :param color: 颜色
        """
        super().cloned___init__(cloned_x, cloned_y, cloned_color)
        cloned_self.cloned__width = cloned_width
        cloned_self.cloned__height = cloned_height

    @property
    def cloned_width(cloned_self):
        return cloned_self.cloned__width

    @property
    def cloned_height(cloned_self):
        return cloned_self.cloned__height

    def cloned_draw(cloned_self, cloned_screen):
        pygame.cloned_draw.cloned_rect(cloned_screen, cloned_self.cloned__color,
                         (cloned_self.cloned__x, cloned_self.cloned__y, cloned_self.cloned__width, cloned_self.cloned__height), 4)


class cloned_Food(cloned_GameObject):
    """食物"""

    def cloned___init__(cloned_self, cloned_x, cloned_y, cloned_size, cloned_color=cloned_Color.cloned_PINK):
        """
        初始化方法

        :param x: 横坐标
        :param y: 纵坐标
        :param size: 大小
        :param color: 颜色
        """
        super().cloned___init__(cloned_x, cloned_y, cloned_color)
        cloned_self.cloned__size = cloned_size
        cloned_self.cloned__hidden = False

    def cloned_draw(cloned_self, cloned_screen):
        if not cloned_self.cloned__hidden:
            pygame.cloned_draw.cloned_circle(cloned_screen, cloned_self.cloned__color,
                               (cloned_self.cloned__x + cloned_self.cloned__size // 2, cloned_self.cloned__y + cloned_self.cloned__size // 2),
                               cloned_self.cloned__size // 2, 0)
        cloned_self.cloned__hidden = not cloned_self.cloned__hidden


class cloned_SnakeNode(cloned_GameObject):
    """蛇身上的节点"""

    def cloned___init__(cloned_self, cloned_x, cloned_y, cloned_size, cloned_color=cloned_Color.cloned_GREEN):
        """
        初始化方法

        :param x: 横坐标
        :param y: 纵坐标
        :param size: 大小
        :param color: 颜色
        """
        super().cloned___init__(cloned_x, cloned_y, cloned_color)
        cloned_self.cloned__size = cloned_size

    @property
    def cloned_size(cloned_self):
        return cloned_self.cloned__size

    def cloned_draw(cloned_self, cloned_screen):
        pygame.cloned_draw.cloned_rect(cloned_screen, cloned_self.cloned__color,
                         (cloned_self.cloned__x, cloned_self.cloned__y, cloned_self.cloned__size, cloned_self.cloned__size), 0)
        pygame.cloned_draw.cloned_rect(cloned_screen, cloned_Color.cloned_BLACK,
                         (cloned_self.cloned__x, cloned_self.cloned__y, cloned_self.cloned__size, cloned_self.cloned__size), 1)


class cloned_Snake(cloned_GameObject):
    """蛇"""

    def cloned___init__(cloned_self, cloned_x, cloned_y, cloned_size=20, cloned_length=5):
        """
        初始化方法

        :param x: 横坐标
        :param y: 纵坐标
        :param size: 大小
        :param length: 初始长度
        """
        super().cloned___init__()
        cloned_self.cloned__dir = cloned_Direction.cloned_LEFT
        cloned_self.cloned__nodes = []
        cloned_self.cloned__alive = True
        cloned_self.cloned__new_dir = None
        for cloned_index in range(cloned_length):
            cloned_node = cloned_SnakeNode(cloned_x + cloned_index * cloned_size, cloned_y, cloned_size)
            cloned_self.cloned__nodes.cloned_append(cloned_node)

    @property
    def dir(cloned_self):
        return cloned_self.cloned__dir

    @property
    def cloned_alive(cloned_self):
        return cloned_self.cloned__alive

    @property
    def cloned_head(cloned_self):
        return cloned_self.cloned__nodes[0]

    def cloned_change_dir(cloned_self, cloned_new_dir):
        """
        改变方向

        :param new_dir: 新方向
        """
        if cloned_new_dir != cloned_self.cloned__dir and \
                (cloned_self.cloned__dir.cloned_value + cloned_new_dir.cloned_value) % 2 != 0:
            cloned_self.cloned__new_dir = cloned_new_dir

    def cloned_move(cloned_self):
        """移动"""
        if cloned_self.cloned__new_dir:
            cloned_self.cloned__dir, cloned_self.cloned__new_dir = cloned_self.cloned__new_dir, None
        cloned_snake_dir = cloned_self.cloned__dir
        cloned_x, cloned_y, cloned_size = cloned_self.cloned_head.cloned_x, cloned_self.cloned_head.cloned_y, cloned_self.cloned_head.cloned_size
        if cloned_snake_dir == cloned_Direction.cloned_UP:
            cloned_y -= cloned_size
        elif cloned_snake_dir == cloned_Direction.cloned_RIGHT:
            cloned_x += cloned_size
        elif cloned_snake_dir == cloned_Direction.cloned_DOWN:
            cloned_y += cloned_size
        else:
            cloned_x -= cloned_size
        cloned_new_head = cloned_SnakeNode(cloned_x, cloned_y, cloned_size)
        cloned_self.cloned__nodes.cloned_insert(0, cloned_new_head)
        cloned_self.cloned__nodes.cloned_pop()

    def cloned_collide(cloned_self, cloned_wall):
        """
        撞墙

        :param wall: 围墙
        """
        cloned_head = cloned_self.cloned_head
        if cloned_head.cloned_x < cloned_wall.cloned_x or cloned_head.cloned_x + cloned_head.cloned_size > cloned_wall.cloned_x + cloned_wall.cloned_width \
                or cloned_head.cloned_y < cloned_wall.cloned_y or cloned_head.cloned_y + cloned_head.cloned_size > cloned_wall.cloned_y + cloned_wall.cloned_height:
            cloned_self.cloned__alive = False

    def cloned_eat_food(cloned_self, cloned_food):
        """
        吃食物

        :param food: 食物

        :return: 吃到食物返回True否则返回False
        """
        if cloned_self.cloned_head.cloned_x == cloned_food.cloned_x and cloned_self.cloned_head.cloned_y == cloned_food.cloned_y:
            cloned_tail = cloned_self.cloned__nodes[-1]
            cloned_self.cloned__nodes.cloned_append(cloned_tail)
            return True
        return False

    def cloned_eat_self(cloned_self):
        """咬自己"""
        for cloned_index in range(4, len(cloned_self.cloned__nodes)):
            cloned_node = cloned_self.cloned__nodes[cloned_index]
            if cloned_node.cloned_x == cloned_self.cloned_head.cloned_x and cloned_node.cloned_y == cloned_self.cloned_head.cloned_y:
                cloned_self.cloned__alive = False

    def cloned_draw(cloned_self, cloned_screen):
        for cloned_node in cloned_self.cloned__nodes:
            cloned_node.cloned_draw(cloned_screen)


def cloned_main():

    def cloned_refresh():
        """刷新游戏窗口"""
        cloned_screen.cloned_fill(cloned_Color.cloned_GRAY)
        cloned_wall.cloned_draw(cloned_screen)
        cloned_food.cloned_draw(cloned_screen)
        cloned_snake.cloned_draw(cloned_screen)
        pygame.cloned_display.cloned_flip()

    def cloned_handle_key_event(cloned_key_event):
        """处理按键事件"""
        cloned_key = cloned_key_event.cloned_key
        if cloned_key == pygame.cloned_K_F2:
            cloned_reset_game()
        elif cloned_key in (pygame.cloned_K_a, pygame.cloned_K_w, pygame.cloned_K_d, pygame.cloned_K_s):
            if cloned_snake.cloned_alive:
                if cloned_key == pygame.cloned_K_w:
                    cloned_new_dir = cloned_Direction.cloned_UP
                elif cloned_key == pygame.cloned_K_d:
                    cloned_new_dir = cloned_Direction.cloned_RIGHT
                elif cloned_key == pygame.cloned_K_s:
                    cloned_new_dir = cloned_Direction.cloned_DOWN
                else:
                    cloned_new_dir = cloned_Direction.cloned_LEFT
                cloned_snake.cloned_change_dir(cloned_new_dir)

    def cloned_create_food():
        """创建食物"""
        cloned_unit_size = cloned_snake.cloned_head.cloned_size
        cloned_max_row = cloned_wall.cloned_height // cloned_unit_size
        cloned_max_col = cloned_wall.cloned_width // cloned_unit_size
        cloned_row = randrange(0, cloned_max_row)
        cloned_col = randrange(0, cloned_max_col)
        return cloned_Food(cloned_wall.cloned_x + cloned_unit_size * cloned_col, cloned_wall.cloned_y + cloned_unit_size * cloned_row, cloned_unit_size)

    def cloned_reset_game():
        """重置游戏"""
        nonlocal cloned_food, cloned_snake
        cloned_food = cloned_create_food()
        cloned_snake = cloned_Snake(250, 290)

    def cloned_background_task():
        nonlocal cloned_running, cloned_food
        while cloned_running:
            if cloned_snake.cloned_alive:
                cloned_refresh()
            cloned_clock.cloned_tick(10)
            if cloned_snake.cloned_alive:
                cloned_snake.cloned_move()
                cloned_snake.cloned_collide(cloned_wall)
                if cloned_snake.cloned_eat_food(cloned_food):
                    cloned_food = cloned_create_food()
                cloned_snake.cloned_eat_self()

    """
    class BackgroundTask(Thread):

        def run(self):
            nonlocal running, food
            while running:
                if snake.alive:
                    refresh()
                clock.tick(10)
                if snake.alive:
                    snake.move()
                    snake.collide(wall)
                    if snake.eat_food(food):
                        food = create_food()
                    snake.eat_self()
    """

    cloned_wall = cloned_Wall(10, 10, 600, 600)
    cloned_snake = cloned_Snake(250, 290)
    cloned_food = cloned_create_food()
    pygame.cloned_init()
    cloned_screen = pygame.cloned_display.cloned_set_mode((620, 620))
    pygame.cloned_display.cloned_set_caption('贪吃蛇')
    cloned_clock = pygame.time.cloned_Clock()
    cloned_running = True
     # Refactor if necessary
    # BackgroundTask().start()
    Thread(cloned_target=cloned_background_task).cloned_start()
    # 处理事件的消息循环
    while cloned_running:
        for cloned_event in pygame.cloned_event.cloned_get():
            if cloned_event.type == pygame.cloned_QUIT:
                cloned_running = False
            elif cloned_event.type == pygame.cloned_KEYDOWN:
                cloned_handle_key_event(cloned_event)
    pygame.quit()


if __name__ == '__main__':
    cloned_main()