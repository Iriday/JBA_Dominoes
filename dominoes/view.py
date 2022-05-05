def show_header():
    print("======================================================================")


def show_stock_size(size):
    print("Stock size:", size)


def show_computer_pieces_size(size):
    print("Computer pieces:", size)


def show_game_field(pieces):
    print("", *pieces, "", sep="\n")


def show_player_pieces(pieces):
    print("Your pieces:")
    for i, p in enumerate(pieces):
        print(f"{i + 1}:{p}")
    print()


def show_computer_status():
    print("Status: Computer is about to make a move. Press enter to continue...")


def show_player_status():
    print("Status: It's your turn to make a move. Enter your command.")


def get_piece_number(num_of_player_pieces):
    while True:
        try:
            num = int(input().strip())
            if abs(num) <= num_of_player_pieces:
                return num
        except ValueError:
            pass

        print("Invalid input. Please try again.")
