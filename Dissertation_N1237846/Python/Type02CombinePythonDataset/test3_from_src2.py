from random import randint
from threading import Thread
from time import sleep

import pygame


class cloned_Color(object):
    cloned_BLACK = (0, 0, 0)
    cloned_WHITE = (255, 255, 255)
    cloned_GRAY = (242, 242, 242)

    @staticmethod
    def cloned_random_color():
        cloned_r = randint(0, 255)
        cloned_g = randint(0, 255)
        cloned_b = randint(0, 255)
        return cloned_r, cloned_g, cloned_b


class cloned_Car(object):

    def cloned___init__(cloned_self, cloned_x, cloned_y, cloned_color):
        cloned_self.cloned__x = cloned_x
        cloned_self.cloned__y = cloned_y
        cloned_self.cloned__color = cloned_color

    def cloned_move(cloned_self):
        if cloned_self.cloned__x + 80 < 950:
            cloned_self.cloned__x += randint(1, 10)

    def cloned_draw(cloned_self, cloned_screen):
        pygame.cloned_draw.cloned_rect(cloned_screen, cloned_self.cloned__color,
                         (cloned_self.cloned__x, cloned_self.cloned__y, 80, 40), 0)


def cloned_main():

    class cloned_BackgroundTask(Thread):

        def cloned_run(cloned_self):
            while True:
                cloned_screen.cloned_fill(cloned_Color.cloned_GRAY)
                pygame.cloned_draw.cloned_line(cloned_screen, cloned_Color.cloned_BLACK, (130, 0), (130, 600), 4)
                pygame.cloned_draw.cloned_line(cloned_screen, cloned_Color.cloned_BLACK, (950, 0), (950, 600), 4)
                for cloned_car in cloned_cars:
                    cloned_car.cloned_draw(cloned_screen)
                pygame.cloned_display.cloned_flip()
                sleep(0.05)
                for cloned_car in cloned_cars:
                    cloned_car.cloned_move()

    cloned_cars = []
    for cloned_index in range(5):
        cloned_temp = cloned_Car(50, 50 + 120 * cloned_index, cloned_Color.cloned_random_color())
        cloned_cars.cloned_append(cloned_temp)
    pygame.cloned_init()
    cloned_screen = pygame.cloned_display.cloned_set_mode((1000, 600))
    cloned_BackgroundTask(cloned_daemon=True).cloned_start()
    cloned_running = True
    while cloned_running:
        for cloned_event in pygame.cloned_event.cloned_get():
            if cloned_event.type == pygame.cloned_QUIT:
                cloned_running = False
    pygame.quit()


if __name__ == '__main__':
    cloned_main()