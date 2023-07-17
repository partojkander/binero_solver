class BineroSolver:

    board = [[0, 1, 1, 0],
             [1, 0, 0, 1],
             [1, 0, 0, 1],
             [0, 1, 1, 0]]

    def print_board(self):
        for row in self.board:
            print(''.join([str(cell) for cell in row]))

    def get_row(self, index):
        return ''.join([str(cell) for cell in self.board[index]])

    def get_column(self, index):
        column = [row[index] for row in self.board]
        return ''.join([str(cell) for cell in column])


if __name__ == '__main__':
    b = BineroSolver()
    print(b.get_row(1))
    print(b.get_column(3))
