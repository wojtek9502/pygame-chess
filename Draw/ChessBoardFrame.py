import pygame

from utils.consts import *
from Draw.Drawable import Drawable


class ChessBoardFrame(Drawable):
    def __init__(self, width, height, x=0, y=0):
        super(ChessBoardFrame, self).__init__(width, height, x, y, BOARD_BACKGROUND_COLOR)

        #draw border on chess board
        chess_board_border_data = [
            CHESS_BOARD_WIDTH_PADDING - CHESS_BOARD_BORDER_SIZE,  # border rectangle start x
            CHESS_BOARD_HEIGHT_PADDING - CHESS_BOARD_BORDER_SIZE, # border rectangle start y
            CHESS_BOARD_WIDTH + (2 * CHESS_BOARD_BORDER_SIZE),    # border rectangle width
            CHESS_BOARD_HEIGHT + (2 * CHESS_BOARD_BORDER_SIZE)    # border rectangle height
        ]
        pygame.draw.rect(self.surface, CHESS_BOARD_BORDER_COLOR, chess_board_border_data)

        # draw baord marks
        vertical_marks = "ABCDEFGH"
        horizontal_marks = reversed("12345678")
        font = pygame.font.Font(None, CHESS_MARKS_FONT_SIZE)

        # write vertical marks
        x = CHESS_BOARD_WIDTH_PADDING + (CHESS_FIELD_LENGHT/2)
        char_x_step = CHESS_FIELD_LENGHT - 1
        for vertical_char in vertical_marks :
            text = font.render(vertical_char, True, CHESS_MARKS_COLOR)

            # write on top of the board
            text_rect = text.get_rect(x=x, y=10)
            self.surface.blit(text, text_rect)

            #write on bottom of the board
            text_rect = text.get_rect(x=x, y=height-20)
            self.surface.blit(text, text_rect)
            x += char_x_step

        # write vertical marks
        y = CHESS_BOARD_HEIGHT_PADDING + (CHESS_FIELD_LENGHT / 2)
        char_y_step = CHESS_FIELD_LENGHT - 1
        for horizontal_char in horizontal_marks:
            text = font.render(horizontal_char, True, CHESS_MARKS_COLOR)

            #write on the left of the board
            text_rect = text.get_rect(x=10, y=y)
            self.surface.blit(text, text_rect)

            #write on the right of the board
            text_rect = text.get_rect(x=width-20, y=y)
            self.surface.blit(text, text_rect)

            y += char_y_step
