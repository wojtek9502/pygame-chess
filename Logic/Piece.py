import pygame

from Draw.Drawable import Drawable
from Logic import ChessBoardField
from utils.PiecesTypesEnum import PiecesTypesEnum
from utils.PlayersEnum import PlayersEnum
from utils.piecesSymbols import PIECES_UNICODE_SYMBOLS_MAP
from utils.consts import *
from utils.piecesTypesStartPosition import PIECES_START_POSITIONS


class Piece(Drawable):
    def __init__(self, chessBoardField: ChessBoardField, pieceType=PiecesTypesEnum.QUEEN, pieceOwner=PlayersEnum.PlayerOne):
        super(Piece, self).__init__(60, 60, chessBoardField.start_x+4, chessBoardField.start_y)
        self.pieceExists = True
        self.pieceOwner = pieceOwner
        self.pieceType = pieceType
        self.pieceSymbol = None
        self.chessBoardFieldX = chessBoardField.row_index
        self.chessBoardFieldY = chessBoardField.col_index
        self.drawPiece()

    def __str__(self):
        return f"{self.pieceOwner.name} {self.pieceType.name} x={self.chessBoardFieldX} y={self.chessBoardFieldY}"

    def drawPiece(self):
        if self.pieceExists:
            self.pieceSymbol = PIECES_UNICODE_SYMBOLS_MAP.get(self.pieceType)
            self.color = PLAYER_ONE_PIECES_COLOR
            if self.pieceOwner is PlayersEnum.PlayerTwo:
                self.color = PLAYER_TWO_PIECES_COLOR

            font = pygame.font.Font("CHEQ_TT.TTF", 55)
            text = font.render(self.pieceSymbol, True, self.color)
            self.surface.blit(text, (0,0))

    @staticmethod
    def createPieceObject(chessBoardField: ChessBoardField):
        for piece_type, pieces_positions in PIECES_START_POSITIONS.items():
            for piece_position in pieces_positions:

                if piece_position == (chessBoardField.row_index, chessBoardField.col_index):
                    piece_owner = PlayersEnum.PlayerOne if chessBoardField.col_index > 5 else PlayersEnum.PlayerTwo
                    piece = Piece(chessBoardField, piece_type, piece_owner)
                    return piece

