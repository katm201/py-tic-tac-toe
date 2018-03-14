class TicTacToe:
    '''Game instance of Tic-Tac-Toe'''
    def __init__(self, player_1, player_2, size):
        self.players = [player_1, player_2]
        self.board = self.__build_board__(size)
        self.currentPlayer = self.players[0]
        self.size = size

    def print_names(self):
        print(self.players)

    def show_current(self):
        print(self.currentPlayer)

    def __build_board__(self, size):
        board = []
        for x in range(size):
            row = []
            for x in range(size):
                row.append('')
            board.append(row)
        return board

    def print_board(self):
        print(self.board)

    def play(self):
        row = input(self.currentPlayer + ' which row would you like? Pick 1 to ' + str(self.size) + ': ')
        column = input(self.currentPlayer + ' which column would you like? Pick 1 to ' + str(self.size) + ': ')
        print(row, column)
