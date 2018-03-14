import tic_tac_toe

def play_game():
    player_1 = input('Player 1, what\'s your name? ')
    player_2 = input('Player 2, what\'s your name? ')
    size = input('How many rows/columns in your board? ')

    game = tic_tac_toe.TicTacToe(player_1, player_2, int(size))
    game.print_names()
    game.show_current()
    game.play()

play_game()
