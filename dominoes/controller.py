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
        v.get_piece_number(len(m.player2_pieces))


run_game()
