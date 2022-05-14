from itertools import combinations_with_replacement
from random import shuffle, randint
from collections import Counter
import numpy as np

INITIAL_PLAYER_PIECES = 7
PLAYER1 = "P1"  # computer
PLAYER2 = "P2"  # player

game_field = []
stock_pieces = ...
player1_pieces = ...
player2_pieces = ...
__current_player = ...


def __generate_pieces():
    return list(map(lambda p: list(p), combinations_with_replacement([0, 1, 2, 3, 4, 5, 6], 2)))


def __shuffle_pieces(pieces):
    shuffle(pieces)
    return pieces


def __pop_n_random_pieces(n, pieces):
    rand_pieces = []
    while len(rand_pieces) < n:
        rand_pieces.append(pieces.pop(randint(0, len(pieces) - 1)))
    return rand_pieces


def __get_initial_player_and_piece(p1_pieces, p2_pieces):
    def get_pieces_with_equal_sides(pieces):
        return [p for p in pieces if p[0] == p[1]]

    def get_largest_piece_with_two_equal_sides(pieces):
        return max(get_pieces_with_equal_sides(pieces), key=lambda p: p[0], default=None)

    def get_initial_player_and_piece(p1_initial_piece, p2_initial_piece):
        if p1_initial_piece and p2_initial_piece:
            return (PLAYER1, p1_initial_piece) if p1_initial_piece[0] > p2_initial_piece[0] else (
                PLAYER2, p2_initial_piece)
        elif p1_initial_piece and not p2_initial_piece:
            return PLAYER1, p1_initial_piece
        elif p2_initial_piece and not p1_initial_piece:
            return PLAYER2, p2_initial_piece
        else:
            return None

    return get_initial_player_and_piece(
        get_largest_piece_with_two_equal_sides(p1_pieces),
        get_largest_piece_with_two_equal_sides(p2_pieces)
    )


def __get_player_pieces_by_player(player):
    return player1_pieces if player == PLAYER1 else player2_pieces


def __switch_player():
    global __current_player
    __current_player = PLAYER1 if __current_player == PLAYER2 else PLAYER2


def __get_piece_by_piece_number(pieces, num):
    return pieces[abs(num) - 1]


def __place_piece_on_game_field(piece_num):
    piece = __get_piece_by_piece_number(__get_current_player_pieces(), piece_num)
    __get_current_player_pieces().remove(piece)
    if piece_num > 0:
        game_field.append(piece)
        if game_field[-1][-2] != game_field[-2][-1]:
            game_field[-1].reverse()
    elif piece_num < 0:
        game_field.insert(0, piece)
        if game_field[0][1] != game_field[1][0]:
            game_field[0].reverse()


def __take_piece_from_stock_and_give_to_curr_player():
    if stock_pieces:
        __get_current_player_pieces().append(stock_pieces.pop(-1))


def __get_current_player_pieces():
    return player1_pieces if __current_player == PLAYER1 else player2_pieces


def __is_piece_of_curr_player_can_be_placed_on_field(piece_number):
    piece = __get_piece_by_piece_number(__get_current_player_pieces(), piece_number)
    return (piece_number < 0 and game_field[0][0] in piece) or (piece_number > 0 and game_field[-1][-1] in piece)


def __is_move_possible(move_num):
    return move_num == 0 or (move_num != 0 and __is_piece_of_curr_player_can_be_placed_on_field(move_num))


def __make_initial_move(piece):
    __get_player_pieces_by_player(get_current_player()).remove(piece)
    game_field.append(piece)
    __switch_player()


def make_move(move_num):
    if not __is_move_possible(move_num):
        return False
    if move_num == 0:
        __take_piece_from_stock_and_give_to_curr_player()
    else:
        __place_piece_on_game_field(move_num)
    __switch_player()
    return True


def get_current_player():
    return __current_player


def get_winner_if_win():
    if not player1_pieces:
        return PLAYER1
    elif not player2_pieces:
        return PLAYER2
    else:
        return None


def is_draw():
    return len(game_field) >= 7 \
           and game_field[0][0] == game_field[-1][-1] \
           and np.count_nonzero(np.array(game_field) == game_field[0][0]) == 8


def start_game():
    def init_fields_and_make_initial_move():
        global stock_pieces, player1_pieces, player2_pieces, __current_player
        while True:
            stock_pieces = __shuffle_pieces(__generate_pieces())
            player1_pieces = __pop_n_random_pieces(INITIAL_PLAYER_PIECES, stock_pieces)
            player2_pieces = __pop_n_random_pieces(INITIAL_PLAYER_PIECES, stock_pieces)
            initial_player_and_piece = __get_initial_player_and_piece(player1_pieces, player2_pieces)

            if initial_player_and_piece:
                __current_player = initial_player_and_piece[0]
                __make_initial_move(initial_player_and_piece[1])
                break

    init_fields_and_make_initial_move()


# AI

def __count_numbers(game_filed_, player_pieces):
    return Counter(np.array(game_filed_ + player_pieces).flatten())


def __prioritise_pieces(counted_nums, player_pieces):
    priority_piece = [[counted_nums[p[0]] + counted_nums[p[1]], p] for p in player_pieces]
    priority_piece.sort(key=lambda v: v[0], reverse=True)
    return [piece for _, piece in priority_piece]


def __get_move_num_by_piece(piece, player_pieces, game_field_):
    if piece in player_pieces:
        i = player_pieces.index(piece) + 1
        if game_field_[-1][-1] in piece:
            return i
        elif game_field_[0][0] in piece:
            return -i
    return 0


def make_computer_move():
    if get_current_player() == PLAYER1:
        for piece in __prioritise_pieces(__count_numbers(game_field, __get_current_player_pieces()), __get_current_player_pieces()):
            move_num = __get_move_num_by_piece(piece, __get_current_player_pieces(), game_field)
            if move_num:
                break
        else:
            move_num = 0
        make_move(move_num)
