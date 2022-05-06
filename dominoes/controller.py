import view as v
import model as m


def run_game():
    m.start_game()
    v.show_header()
    v.show_stock_size(len(m.stock_pieces))
    v.show_computer_pieces_size(len(m.player1_pieces))
    v.show_game_field(m.game_field)
    v.show_player_pieces(m.player2_pieces)

    if m.current_player == m.PLAYER1:
        v.show_computer_status()
    elif m.current_player == m.PLAYER2:
        v.show_player_status()
        piece_number = v.get_piece_number(len(m.player2_pieces))
        piece = m.get_piece_by_number(m.player2_pieces, piece_number)
        side = m.calc_field_side_by_piece_number(piece_number)
        m.make_move(m.PLAYER2, piece, side)

    v.show_game_field(m.game_field)


run_game()
