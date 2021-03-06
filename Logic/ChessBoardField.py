import pygame

from Draw.Drawable import Drawable


class ChessBoardField(Drawable):
    def __init__(self, width, height, x, y, row_index, col_index, color=(255, 0, 0)):
        super(ChessBoardField, self).__init__(width, height, x, y, color)
        pygame.draw.rect(self.surface, self.color, [0, 0, self.width, self.height])
        self.start_x = x
        self.start_y = y
        self.row_index = col_index
        self.col_index = row_index

    def __str__(self):
        return f"{self.row_index}x{self.col_index}"