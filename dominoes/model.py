from itertools import combinations_with_replacement
from random import shuffle

INITIAL_PLAYER_PIECES = 7
PLAYER1 = "P1"
PLAYER2 = "P2"


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
            return (PLAYER1, p1_initial_piece) if p1_initial_piece[0] > p2_initial_piece[0] else (PLAYER2, p2_initial_piece)
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


stock_pieces = __shuffle_pieces(__generate_pieces())
computer_pieces = __pop_n_pieces(INITIAL_PLAYER_PIECES, stock_pieces)
player_pieces = __pop_n_pieces(INITIAL_PLAYER_PIECES, stock_pieces)
