import pygame

from Logic.ChessBoard import ChessBoard
from utils.consts import CHESS_FIELD_LENGHT, NUMBER_OF_ROWS_ON_CHESS_BOARD, NUMBER_OF_COLS_ON_CHESS_BOARD


class Mouse:

    @staticmethod
    def getFieldUnderMouse(chessBoard: ChessBoard):
        board_pos = (chessBoard.boardPositionX, chessBoard.boardPositionY)
        mouse_curr_coordinates = pygame.Vector2(pygame.mouse.get_pos()) - board_pos

        mouse_x_cord = int(mouse_curr_coordinates[0])
        mouse_y_cord = int(mouse_curr_coordinates[1])

        x = chess_board_field_column_under_mouse = mouse_x_cord // CHESS_FIELD_LENGHT
        y = chess_board_field_row_under_mouse = mouse_y_cord // CHESS_FIELD_LENGHT

        if x < 0 or x > NUMBER_OF_COLS_ON_CHESS_BOARD-1:
            return False, False, False

        if y < 0 or y > NUMBER_OF_ROWS_ON_CHESS_BOARD-1:
            return False, False, False

        chess_board_field_under_mouse = chessBoard.getChessBoardField(x,y)
        print(chess_board_field_under_mouse, x, y)
        return chess_board_field_under_mouse, x,y
