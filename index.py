import tic_tac_toe

def play_game():
    '''Logic for building tic-tac-toe instance and playing rounds'''

    player_1 = input('Player 1, what\'s your name? ')
    player_2 = input('Player 2, what\'s your name? ')
    size = input('How many rows/columns in your board? Minimum size is 3, maximum size is 8: ')

    game = tic_tac_toe.TicTacToe(player_1, player_2, int(size))
    
    outcome = game.play()
    while outcome != 'ended':
      outcome = game.play()

play_game()
