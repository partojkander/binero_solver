from typing import List

from exceptions import (
    BineroEmptyCellsException,
    BineroMismatchingCountException,
    BineroThreeOnesException,
    BineroThreeZeroesException
)


class BineroBoard:

    board = ['0110',
             '1100',
             '1001',
             '0110']

    def print_board(self):
        print('\n'.join([row for row in self.board]))

    def get_row(self, index) -> str:
        return self.board[index]

    def get_column(self, index) -> str:
        return ''.join([row[index] for row in self.board])

    def get_rows(self) -> List[str]:
        return self.board

    def get_columns(self) -> List[str]:
        columns = []
        for index in range(len(self.board[0])):
            columns.append(''.join([row[index] for row in self.board]))
        return columns

    def is_valid_sequence(self, sequence: str) -> bool:
        print(f"Validating sequence '{sequence}'")
        if '000' in sequence:
            raise BineroThreeZeroesException(f"Err: sequence '{sequence}' contains '000'")
        if '111' in sequence:
            raise BineroThreeOnesException(f"Err: sequence '{sequence}' contains '111'")
        if ' ' in sequence:
            raise BineroEmptyCellsException(f"Err: sequence '{sequence}' contains empty cell(s)")
        if sequence.count('0') != sequence.count('1'):
            raise BineroMismatchingCountException(f"Err: sequence '{sequence}' has different amount of 1's and 0's")

        return True

    def is_board_solved(self):
        print("Validating rows...")
        for row in self.get_rows():
            if not self.is_valid_sequence(row):
                return False
        print("Validating columns...")
        for column in self.get_columns():
            if not self.is_valid_sequence(column):
                return False

        return True


if __name__ == '__main__':
    b = BineroBoard()
    print(b.is_board_solved())
