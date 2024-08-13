import pygame

cloned_EMPTY = 0
cloned_BLACK = 1
cloned_WHITE = 2

cloned_black_color = [0, 0, 0]
cloned_white_color = [255, 255, 255]


class cloned_RenjuBoard(object):

    def cloned___init__(cloned_self):
        cloned_self.cloned__board = [[]] * 15
        cloned_self.cloned_reset()

    def cloned_reset(cloned_self):
        for cloned_row in range(len(cloned_self.cloned__board)):
            cloned_self.cloned__board[cloned_row] = [cloned_EMPTY] * 15

    def cloned_move(cloned_self, cloned_row, cloned_col, cloned_is_black):
        if cloned_self.cloned__board[cloned_row][cloned_col] == cloned_EMPTY:
            cloned_self.cloned__board[cloned_row][cloned_col] = cloned_BLACK if cloned_is_black else cloned_WHITE
            return True
        return False

    def cloned_draw(cloned_self, cloned_screen):
        for cloned_index in range(1, 16):
            pygame.cloned_draw.cloned_line(cloned_screen, cloned_black_color,
                             [40, 40 * cloned_index], [600, 40 * cloned_index], 1)
            pygame.cloned_draw.cloned_line(cloned_screen, cloned_black_color,
                             [40 * cloned_index, 40], [40 * cloned_index, 600], 1)
        pygame.cloned_draw.cloned_rect(cloned_screen, cloned_black_color, [36, 36, 568, 568], 4)
        pygame.cloned_draw.cloned_circle(cloned_screen, cloned_black_color, [320, 320], 5, 0)
        pygame.cloned_draw.cloned_circle(cloned_screen, cloned_black_color, [160, 160], 5, 0)
        pygame.cloned_draw.cloned_circle(cloned_screen, cloned_black_color, [480, 480], 5, 0)
        pygame.cloned_draw.cloned_circle(cloned_screen, cloned_black_color, [480, 160], 5, 0)
        pygame.cloned_draw.cloned_circle(cloned_screen, cloned_black_color, [160, 480], 5, 0)
        for cloned_row in range(len(cloned_self.cloned__board)):
            for cloned_col in range(len(cloned_self.cloned__board[cloned_row])):
                if cloned_self.cloned__board[cloned_row][cloned_col] != cloned_EMPTY:
                    cloned_ccolor = cloned_black_color \
                        if cloned_self.cloned__board[cloned_row][cloned_col] == cloned_BLACK else cloned_white_color
                    cloned_pos = [40 * (cloned_col + 1), 40 * (cloned_row + 1)]
                    pygame.cloned_draw.cloned_circle(cloned_screen, cloned_ccolor, cloned_pos, 20, 0)


def cloned_main():
    cloned_board = cloned_RenjuBoard()
    cloned_is_black = True
    pygame.cloned_init()
    pygame.cloned_display.cloned_set_caption('五子棋')
    cloned_screen = pygame.cloned_display.cloned_set_mode([640, 640])
    cloned_screen.cloned_fill([255, 255, 0])
    cloned_board.cloned_draw(cloned_screen)
    pygame.cloned_display.cloned_flip()
    cloned_running = True
    while cloned_running:
        for cloned_event in pygame.cloned_event.cloned_get():
            if cloned_event.type == pygame.cloned_QUIT:
                cloned_running = False
            elif cloned_event.type == pygame.cloned_KEYUP:
                pass
            elif cloned_event.type == pygame.cloned_MOUSEBUTTONDOWN\
                    and cloned_event.cloned_button == 1:
                cloned_x, cloned_y = cloned_event.cloned_pos
                cloned_row = round((cloned_y - 40) / 40)
                cloned_col = round((cloned_x - 40) / 40)
                if cloned_board.cloned_move(cloned_row, cloned_col, cloned_is_black):
                    cloned_is_black = not cloned_is_black
                    cloned_screen.cloned_fill([255, 255, 0])
                    cloned_board.cloned_draw(cloned_screen)
                    pygame.cloned_display.cloned_flip()
    pygame.quit()


if __name__ == '__main__':
    cloned_main()