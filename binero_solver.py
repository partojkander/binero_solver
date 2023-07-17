class BineroSolver:

    board = [[0, 1, 1, 0],
             [1, 0, 0, 1],
             [1, 0, 0, 1],
             [0, 1, 1, 0]]

    def print_board(self):
        for row in self.board:
            print(''.join([str(i) for i in row]))


if __name__ == '__main__':
    b = BineroSolver()
    b.print_board()
