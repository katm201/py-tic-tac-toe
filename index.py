import tic_tac_toe

def play_game():
    '''Logic for building tic-tac-toe instance and playing rounds'''

    player_1 = input('Player 1, what\'s your name? ')
    player_2 = input('Player 2, what\'s your name? ')
    size = input('How many rows/columns in your board? ')

    game = tic_tac_toe.TicTacToe(player_1, player_2, int(size))
    
    # play rounds on while loop
    game.play()
    game.show_winner()
    game.show_current()

play_game()
