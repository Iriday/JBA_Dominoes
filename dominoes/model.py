from itertools import combinations_with_replacement
from random import shuffle


def generate_pieces_random_order():
    pieces = list(map(lambda p: list(p), combinations_with_replacement([0, 1, 2, 3, 4, 5, 6], 2)))
    shuffle(pieces)
    return pieces
