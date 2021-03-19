import pygame

from Draw.Drawable import Drawable


class ChessBoardField(Drawable):
    def __init__(self, width, height, x, y, col_index, row_index, color=(255, 0, 0)):
        super(ChessBoardField, self).__init__(width, height, x, y, color)
        pygame.draw.rect(self.surface, self.color, [0, 0, self.width, self.height])
        self.start_x = x
        self.start_y = y
        self.row_index = row_index
        self.col_index = col_index
        self.piece = None

    def __str__(self):
        is_piece_on_field = False if not self.piece else self.piece
        str_ = f"{self.row_index}x{self.col_index} {self.piece}"

        return str_