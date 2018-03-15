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
        # print win or loss message
        self.status = 'ended'
        return self.status

    def __validate_config__(self):
        # check name/info for each player
        # check board size
        return True

    def __update_config__(self):
        # updates an invalid config
        pass

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
            # run validate config logic
            # if valid, update status
            # if not valid, run update config logic on while loop so it'll keep going until there's a problem
            pass

        if self.status == 'ended':
            # print message that the game has ended
            return self.status

        row = self.__pick_move__('row')
        column = self.__pick_move__('column')
        valid_move = self.__validate_move__(row, column)
        while not valid_move:
            print('I\'m sorry, that\'s not a valid move. ')
            # have them pick new moves and re-validate

        win = self.__check_win__()
        if win:
            self.__show_outcome__('win')

        loss = self.__check_loss__()
        if loss:
            self.__show_outcome__('loss')

        self.__render__()
        self.turn = not self.turn
        self.currentPlayer = self.players[self.turn]
        return self.status
