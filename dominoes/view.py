import model as m


def show_header():
    print("======================================================================")


def show_stock_size(size):
    print("Stock size:", size)


def show_computer_pieces_size(size):
    print("Computer pieces:", size)


def show_game_field(pieces):
    print("\n", *(pieces if len(pieces) <= 6 else pieces[:3] + ["..."] + pieces[-3:]), "\n", sep="")


def show_player_pieces(pieces):
    print("Your pieces:")
    for i, p in enumerate(pieces):
        print(f"{i + 1}:{p}")
    print()


def show_status(player):
    if player == m.PLAYER1:
        print("Status: Computer is about to make a move. Press enter to continue...")
    elif player == m.PLAYER2:
        print("Status: It's your turn to make a move. Enter your command.")


def show_win(winner):
    if winner == m.PLAYER1:
        print("Status: The game is over. The computer won!")
    elif winner == m.PLAYER2:
        print("Status: The game is over. You won!")


def show_draw():
    print("Status: The game is over. It's a draw!")


def show_illegal_move_err():
    print("Illegal move. Please try again.")


def get_move_num(num_of_player_pieces):
    while True:
        try:
            num = int(input().strip())
            if abs(num) <= num_of_player_pieces:
                return num
        except ValueError:
            pass

        print("Invalid input. Please try again.")


def get_any_input():
    return input()
