from stockfish import Stockfish

import keyboard

stockfish = Stockfish("stockfish_13_win_x64.exe")

def clear_console():
    import os
    clear = lambda: os.system('cls')
    clear()


game_moves_list = []
while True:
    clear_console()
    best_move = stockfish.get_best_move()
    game_moves_list.append(best_move)
    stockfish.set_position(game_moves_list)
    print(stockfish.get_board_visual())
    while not keyboard.is_pressed('space'):
        continue


