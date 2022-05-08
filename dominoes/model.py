from itertools import combinations_with_replacement
from random import shuffle, randint
import numpy as np

INITIAL_PLAYER_PIECES = 7
PLAYER1 = "P1"  # computer
PLAYER2 = "P2"  # player
LEFT = "LEFT"
RIGHT = "RIGHT"

game_field = []
stock_pieces = ...
player1_pieces = ...
player2_pieces = ...
current_player = ...


def __generate_pieces():
    return list(map(lambda p: list(p), combinations_with_replacement([0, 1, 2, 3, 4, 5, 6], 2)))


def __shuffle_pieces(pieces):
    shuffle(pieces)
    return pieces


def __pop_n_pieces(n, pieces):
    return [pieces.pop() for _ in range(n)]


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
    global current_player
    current_player = PLAYER1 if current_player == PLAYER2 else PLAYER2


def get_piece_by_number(pieces, num):
    return pieces[abs(num) - 1]


def calc_field_side_by_piece_number(num):
    return LEFT if num < 0 else RIGHT


def make_move(piece, side):
    __get_player_pieces_by_player(current_player).remove(piece)
    if side == RIGHT:
        game_field.append(piece)
    elif side == LEFT:
        game_field.insert(0, piece)
    __switch_player()


def take_piece_from_stock_and_give_to_player():
    if stock_pieces:
        get_current_player_pieces().append(stock_pieces.pop(-1))
    __switch_player()


def get_random_piece_number(player_pieces_len):
    return randint(-player_pieces_len, player_pieces_len)


def get_current_player_pieces():
    return player1_pieces if current_player == PLAYER1 else player2_pieces


def is_piece_can_be_placed_on_field(piece_number):
    piece = get_piece_by_number(get_current_player_pieces(), piece_number)
    return (piece_number < 0 and game_field[0][0] in piece) or (piece_number > 0 and game_field[-1][-1] in piece)


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
        global stock_pieces, player1_pieces, player2_pieces, current_player
        while True:
            stock_pieces = __shuffle_pieces(__generate_pieces())
            player1_pieces = __pop_n_pieces(INITIAL_PLAYER_PIECES, stock_pieces)
            player2_pieces = __pop_n_pieces(INITIAL_PLAYER_PIECES, stock_pieces)
            initial_player_and_piece = __get_initial_player_and_piece(player1_pieces, player2_pieces)

            if initial_player_and_piece:
                current_player = initial_player_and_piece[0]
                make_move(initial_player_and_piece[1], RIGHT)
                break

    init_fields_and_make_initial_move()
