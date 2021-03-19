from utils.consts import *
from Logic.ChessBoardField import ChessBoardField
from Logic.Piece import Piece


class ChessBoard:
    def __init__(self, board_start_x, board_start_y):
        self.boardFieldsMatrix = self.setBoard(board_start_x, board_start_y)
        self.setPiecesOnStartPosition()
        self.boardPositionX = board_start_x
        self.boardPositionY = board_start_y

    def setBoard(self, x, y):
        boardFieldsMatrix = []
        start_x = x
        start_y = y
        for col_index in range(NUMBER_OF_COLS_ON_CHESS_BOARD):
            boardFieldsMatrix.append([])
            for row_index in range(NUMBER_OF_ROWS_ON_CHESS_BOARD):
                fieldColor = self.getChessBoardFieldColor(col_index, row_index)
                boardField = ChessBoardField(CHESS_FIELD_LENGHT, CHESS_FIELD_LENGHT, start_x, start_y,
                                             row_index=row_index, col_index=col_index, color=fieldColor)
                start_x += CHESS_FIELD_LENGHT
                if start_x >= CHESS_FIELD_LENGHT * NUMBER_OF_ROWS_ON_CHESS_BOARD:
                    start_x = x
                    start_y += CHESS_FIELD_LENGHT
                boardFieldsMatrix[col_index].append(boardField)
        return boardFieldsMatrix

    def getPiecesOnBoardList(self):
        _list = list()
        for chess_board_row in self.boardFieldsMatrix:
            for chessBoardField in chess_board_row:
                piece = chessBoardField.piece
                if piece:
                    _list.append(chessBoardField.piece)
                    piece.drawPiece()
        return _list

    def setPiecesOnStartPosition(self):
        for row in self.boardFieldsMatrix:
            for field in row:
                if field.col_index < 2 or field.col_index > 5:
                    piece = Piece.createPieceObject(field)
                    field.piece = piece

    def getChessBoardFieldColor(self, col_index, row_index):
        if col_index & 1 == 0:
            return FIRST_FIELD_COLOR if row_index & 1 == 0 else SECOND_FIELD_COLOR

        return SECOND_FIELD_COLOR if row_index & 1 == 0 else FIRST_FIELD_COLOR

    def getChessBoardField(self, board_row, board_col):
        for cols in self.boardFieldsMatrix:
            for chessBoardField in cols:
                if chessBoardField.row_index == board_row and \
                   chessBoardField.col_index == board_col:
                    return chessBoardField

        return False
