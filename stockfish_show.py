import random
import os

from stockfish import Stockfish
import keyboard

stockfish = Stockfish("stockfish.exe")
stockfish_skill_lvl = random.randint(20, 100)
stockfish_depth = random.randint(6, 11)

is_white_turn = True
game_moves_list = []

stockfish_info_str = f"{'#' * 20}\nStockfish info:\nskill level: {stockfish_skill_lvl}\ndepth: {stockfish_depth}\n{'#' * 20}\n\n"
player_str = "White" if is_white_turn else "Black"
next_turn_help_str = "\n\nPress space..."


def clear_console():
    clear = lambda: os.system('cls')
    clear()


def print_game_turn(*arg):
    print(*arg)


def set_random_stockfish_stats(stockfish: Stockfish, stockfish_skill_lvl, stockfish_depth):
    stockfish.set_skill_level(stockfish_skill_lvl)
    stockfish.set_depth(stockfish_depth)
    return stockfish


if __name__ == "__main__":
    stockfish = set_random_stockfish_stats(stockfish, stockfish_skill_lvl, stockfish_depth)
    while True:
        clear_console()

        best_move = stockfish.get_best_move()
        if best_move is None:
            break

        game_moves_list.append(best_move)
        stockfish.set_position(game_moves_list)

        player_str = "White" if is_white_turn else "Black"
        turn_str = f"\nPlayer {player_str} move: {best_move}"
        print_game_turn(stockfish_info_str, stockfish.get_board_visual(), turn_str, next_turn_help_str)

        is_white_turn = False if is_white_turn == True else True

        while not keyboard.is_pressed('space'):
            continue

    print_game_turn(stockfish_info_str, stockfish.get_board_visual(), turn_str)
    print(f"\n{player_str} won")
