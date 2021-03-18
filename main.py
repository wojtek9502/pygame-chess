import pygame

import pygame
import pygame.locals
import itertools

from Draw.ChessBoardFrame import ChessBoardFrame
from Logic.ChessBoard import ChessBoard
from utils.consts import *


class GameWindow:
    """
    Plansza do gry. Odpowiada za rysowanie okna gry.
    """

    def __init__(self, width, height):
        """
        Konstruktor planszy do gry. Przygotowuje okienko gry.

        :param width:
        :param height:
        """
        self.surface = pygame.display.set_mode((width, height), 0, 32)
        pygame.display.set_caption('Chess')

    def draw(self, *args):
        """
        Rysuje okno gry

        :param args: lista obiektów do narysowania
        """
        self.surface.fill(BOARD_BACKGROUND_COLOR)
        for drawable in args:
            drawable.draw_on(self.surface)

        # dopiero w tym miejscu następuje fatyczne rysowanie
        # w oknie gry, wcześniej tylko ustalaliśmy co i jak ma zostać narysowane
        pygame.display.update()



class ChessGame():
    """
    Łączy wszystkie elementy gry w całość.
    """

    def __init__(self, width, height):
        pygame.init()
        pygame.font.init()
        self.gameWindow = GameWindow(width, height)
        # zegar którego użyjemy do kontrolowania szybkości rysowania
        # kolejnych klatek gry
        self.fps_clock = pygame.time.Clock()
        self.chessBoardFrame = ChessBoardFrame(width, height)

        board_start_x = CHESS_BOARD_WIDTH_PADDING
        board_start_y = CHESS_BOARD_HEIGHT_PADDING
        self.chessBoard = ChessBoard(board_start_x=board_start_x, board_start_y=board_start_y)



    def run(self):
        """
        Główna pętla programu
        """
        while not self.handle_events():
            # działaj w pętli do momentu otrzymania sygnału do wyjścia
            self.gameWindow.draw(
                self.chessBoardFrame,
                # split 2d list (boardFieldsMatrix) to 1d list and unpack it with *
                # every list elem is chess board field
                *list(itertools.chain.from_iterable(self.chessBoard.boardFieldsMatrix)),
                *self.chessBoard.getPiecesOnBoardList(),

            )
            self.fps_clock.tick(30)


    def handle_events(self):
        """
        Obsługa zdarzeń systemowych, tutaj zinterpretujemy np. ruchy myszką

        :return True jeżeli pygame przekazał zdarzenie wyjścia z gry
        """
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True


# Ta część powinna być zawsze na końcu modułu (ten plik jest modułem)
# chcemy uruchomić naszą grę dopiero po tym jak wszystkie klasy zostaną zadeklarowane
if __name__ == "__main__":
    game = ChessGame(WINDOW_WIDTH, WINDOW_HEIGHT)
    game.run()