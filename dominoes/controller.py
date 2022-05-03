import view as v
import model as m


def run_game():
    m.start_game()
    v.show_header()
    v.show_stock_size(len(m.stock_pieces))
    v.show_computer_pieces_size(len(m.player1_pieces))
    v.show_game_field(m.game_field)
    v.show_player_pieces(m.player2_pieces)
    v.show_status(m.current_player)


run_game()
