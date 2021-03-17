from utils.consts import *
from Logic.ChessBoardField import ChessBoardField
from Logic.Piece import Piece


class ChessBoard:
    def __init__(self, board_start_x, board_start_y, ):
        self.boardFieldsMatrix = self.generateChessBoardFields(board_start_x, board_start_y)

    def generateChessBoardFields(self, x, y):
        boardFieldsMatrix = []
        start_x = x
        start_y = y
        for col_index in range(NUMBER_OF_COLS_ON_CHESS_BOARD):
            boardFieldsMatrix.append([])
            for row_index in range(NUMBER_OF_ROWS_ON_CHESS_BOARD):
                fieldColor = self.getChessBoardFieldColor(FIRST_FIELD_COLOR, SECOND_FIELD_COLOR, col_index, row_index)
                boardField = ChessBoardField(CHESS_FIELD_LENGHT, CHESS_FIELD_LENGHT, start_x, start_y, row_index,
                                             col_index, fieldColor)
                start_x += CHESS_FIELD_LENGHT
                if start_x >= CHESS_FIELD_LENGHT * NUMBER_OF_ROWS_ON_CHESS_BOARD:
                    start_x = x
                    start_y += CHESS_FIELD_LENGHT
                boardFieldsMatrix[col_index].append(boardField)
        return boardFieldsMatrix

    def getChessBoardFieldColor(self, first_color, second_color, col_index, row_index):
        if col_index & 1 == 0:
            return first_color if row_index & 1 == 0 else second_color

        return second_color if row_index & 1 == 0 else first_color

    def setPieces(self):
        PiecesObjectsList = []
        for col in self.boardFieldsMatrix:
            for field in col:
                if field.row_index < 2 or field.row_index > 5:
                    piece = Piece(field)
                    PiecesObjectsList.append(piece)
        return PiecesObjectsList
