import os

class TicTacToe:
    '''Game instance of Tic-Tac-Toe'''
    def __init__(self, player_1, player_2, size):
        self.players = [player_1, player_2]
        self.markers = ['X', 'O']
        self.turn = 0
        self.currentPlayer = self.players[self.turn]
        self.size = size
        self.board = self.__build_board__(size)
        self.winner = None
        self.status = 'started'

    def __show_outcome__(self, outcomeType):
        if outcomeType == 'win':
            print('Congratulations ' + self.winner + '! You\'ve won.')

        if outcomeType == 'no_wins':
            print('No more win conditions possible with the current moves available. Please play again!')

        self.status = 'ended'
        return self.status

    def __validate_config__(self):
        return self.players[0] != self.players[1] and self.size > 2 and self.size < 9

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
        return row < self.size and column < self.size and self.board[row][column] == ' '

    def __check_segment__(self, segment, checkType, marker):
        consistent = True
        for position in range(self.size):
            if checkType == 'row':
                consistent = self.board[segment][position] == marker
            else:
                consistent = self.board[position][segment] == marker

            if not consistent:
                return False

        return True

    def __check_segments__(self, checkType, marker):
        for segment in range(self.size):
            if not self.__check_segment__(segment, checkType, marker):
                return False

        return True

    def __check_diagonals__(self, marker):
        for segment in range(self.size):
            if self.board[segment][segment] != marker:
                return False

        for segment in range(self.size):
            if self.board[segment][self.size - segment - 1] != marker:
                return False

        return True

    def __check_condition__(self, conditionType):
        if conditionType == 'win':
            marker = self.markers[self.turn]
        else:
            marker = ' '

        condition = self.__check_segments__('row', marker)
        if condition:
            return True
        
        condition = self.__check_segments__('row', marker)
        if condition:
            return True
        
        return self.__check_diagonals__(marker)

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
        move = input(self.currentPlayer + ', which ' + moveType + ' would you like? Pick 1 to ' + str(self.size) + ': ')
        return int(move) - 1

    def play(self):
        if self.status = 'in-progress':
            os.system('cls||clear')

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
            valid_move = self.__validate_move__(row, column)

        self.board[row][column] = self.markers[self.turn]

        win = self.__check_condition__('win')
        if win:
            return self.__show_outcome__('win')

        no_wins = self.__check_condition__('no_wins')
        if no_wins:
            return self.__show_outcome__('no_wins')

        self.__render__()
        self.turn = not self.turn
        self.currentPlayer = self.players[self.turn]
        return self.status
