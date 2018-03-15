class TicTacToe:
    '''Game instance of Tic-Tac-Toe'''
    def __init__(self, player_1, player_2, size):
        self.players = [player_1, player_2]
        self.turn = 0
        self.currentPlayer = self.players[self.turn]
        self.size = size
        self.board = self.__build_board__(size)
        self.winner = None
        self.status = 'started'

    def __show_outcome__(self, outcomeType):
        if outcomeType == 'win':
            print('Congratulations ' + self.winner + '! You\'ve won.')

        if outcomeType == 'loss':
            print('No more win conditions possible with the current moves available. Please play again!')

        self.status = 'ended'
        return self.status

    def __validate_config__(self):
        return self.players[0] != self.players[1] && self.size > 2 && self.size < 9:

    def __update_config__(self):
        print('I\'m sorry, that\'s not a valid game setup. ')
        player_1 = input('Player 1, what\'s your name? You must enter a unique name. ')
        player_2 = input('Player 2, what\'s your name? You must enter a unique name. ')
        size = input('How many rows/columns in your board? Minimum size is 3, maximum size is 8: ')
        self.players = [player_1, player_2]
        self.size = size
        self.currentPlayer = self.players[self.turn]
        self.board = self.__build_board__(size)

    def __validate_move__(self, row, column):
        # check if in the proper range
        # check if available
        return True

    def __check_win__(self):
        # checks to see if a player has won
        return True

    def __check_loss__(self):
        # checks to see if there are any possible win conditions
        return True

    def __build_board__(self, size):
        board = []
        for x in range(size):
            row = []
            for x in range(size):
                row.append(' ')
            board.append(row)
        return board

    def __render__(self):
        rows = list(map(lambda row: '\n ' + ' | '.join(row) + ' \n', self.board))
        board = '___ ___ ___\n'.join(rows)
        print(board)

    def __pick_move__(self, moveType):
        move = input(self.currentPlayer + ' which ' + moveType + ' would you like? Pick 1 to ' + str(self.size) + ': ')
        return move

    def play(self):
        if self.status == 'started':
            valid_config = self.__validate_config__()
            if not valid_config:
                self.__update_config__()
                valid_config = self.__validate_config__()

            self.status = 'in-progress'

        if self.status == 'ended':
            print('I\'m sorry, the game has ended. Please start a new game to play.')
            return self.status

        row = self.__pick_move__('row')
        column = self.__pick_move__('column')
        valid_move = self.__validate_move__(row, column)
        while not valid_move:
            print('I\'m sorry, that\'s not a valid move. ')
            row = self.__pick_move__('row')
            column = self.__pick_move__('column')

        win = self.__check_win__()
        if win:
            return self.__show_outcome__('win')

        loss = self.__check_loss__()
        if loss:
            return self.__show_outcome__('loss')

        self.__render__()
        self.turn = not self.turn
        self.currentPlayer = self.players[self.turn]
        return self.status
