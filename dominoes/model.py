from itertools import combinations_with_replacement
from random import shuffle

INITIAL_PLAYER_PIECES = 7


def __generate_pieces():
    return list(map(lambda p: list(p), combinations_with_replacement([0, 1, 2, 3, 4, 5, 6], 2)))


def __shuffle_pieces(pieces):
    shuffle(pieces)
    return pieces


def __pop_n_pieces(n, pieces):
    return [pieces.pop() for _ in range(n)]


stock_pieces = __shuffle_pieces(__generate_pieces())
computer_pieces = __pop_n_pieces(INITIAL_PLAYER_PIECES, stock_pieces)
player_pieces = __pop_n_pieces(INITIAL_PLAYER_PIECES, stock_pieces)
