class TicTacToe:
    '''Game instance of Tic-Tac-Toe'''
    def __init__(self, player_1, player_2, size):
        self.players = [player_1, player_2]
        self.turn = 0
        self.currentPlayer = self.players[self.turn]
        self.size = size
        self.board = self.__build_board__(size)
        self.winner = None

    def show_current(self):
        print(self.currentPlayer)

    def show_winner(self):
        print(self.winner)

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

    def play(self):

        row = input(self.currentPlayer + ' which row would you like? Pick 1 to ' + str(self.size) + ': ')
        column = input(self.currentPlayer + ' which column would you like? Pick 1 to ' + str(self.size) + ': ')
        self.__render__()
        self.turn = not self.turn
        self.currentPlayer = self.players[self.turn]
