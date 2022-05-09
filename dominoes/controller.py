import view as v
import model as m


def run_game():
    m.start_game()
    while True:
        # show state
        v.show_header()
        v.show_stock_size(len(m.stock_pieces))
        v.show_computer_pieces_size(len(m.player1_pieces))
        v.show_game_field(m.game_field)
        v.show_player_pieces(m.player2_pieces)

        # game over check
        winner = m.get_winner_if_win()
        if winner:
            v.show_win(winner)
            return
        elif m.is_draw():
            v.show_draw()
            return

        # make move
        v.show_status(m.get_current_player())
        if m.get_current_player() == m.PLAYER1:
            v.get_any_input()
            move_num = m.get_random_move_num(len(m.get_current_player_pieces()))
            m.make_move(move_num)
        elif m.get_current_player() == m.PLAYER2:
            while True:
                move_num = v.get_move_num(len(m.get_current_player_pieces()))
                if m.is_move_possible(move_num):
                    m.make_move(move_num)
                    break
                else:
                    v.show_illegal_move_err()


run_game()
