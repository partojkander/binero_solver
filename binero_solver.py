from copy import copy

from binero_board import BineroBoard


class BineroSolver:

    board = None

    def __init__(self, size):
        self.board = BineroBoard(size=size)

    def fill_around_double(self, sequence: str) -> str:
        sequence = sequence.replace(' 00', '100')
        sequence = sequence.replace('00 ', '001')
        sequence = sequence.replace(' 11', '011')
        sequence = sequence.replace('11 ', '110')
        return sequence

    def fill_gap(self, sequence: str) -> str:
        sequence = sequence.replace('0 0', '010')
        sequence = sequence.replace('1 1', '101')
        return sequence

    def apply_solutions(self):
        while True:
            old_board = copy(self.board.get_board())
            for row_index, row in enumerate(self.board.get_rows()):
                row = self.fill_around_double(row)
                row = self.fill_gap(row)
                self.board.set_row(row_index, row)
            for column_index, column in enumerate(self.board.get_columns()):
                column = self.fill_around_double(column)
                column = self.fill_gap(column)
                self.board.set_column(column_index, column)
            if self.board.get_board() == old_board:
                print("No more solutions available, exiting...")
                break
