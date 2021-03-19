import pygame

from Draw.Drawable import Drawable
from Logic import ChessBoardField

class Piece(Drawable):

    def __init__(self, chessBoardField: ChessBoardField):
        super(Piece, self).__init__(30, 30, chessBoardField.start_x + 15, chessBoardField.start_y + 15)
        self.exists = True
        self.color = (255, 255, 255)
        self.drawPiece()

    def drawPiece(self):
        if self.exists:
            pygame.draw.rect(self.surface, self.color, [0, 0, self.width, self.height])