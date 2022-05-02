import view as v
import model as m


def run_game():
    m.start_game()
    v.show_stock_pieces(m.stock_pieces)
    v.show_computer_pieces(m.player1_pieces)
    v.show_player_pieces(m.player2_pieces)
    v.show_domino_snake(m.domino_snake)
    v.show_status("player" if m.current_player == m.PLAYER2 else "computer")


run_game()
