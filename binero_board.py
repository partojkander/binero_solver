from typing import List


class BineroBoard:

    _board = []

    def __init__(self, size):
        if size % 2 != 0:
            raise ValueError("Error, board cannot have odd number of rows/columns")

        self._board = [' '*size] * size

    def get_row(self, index: int) -> str:
        return self._board[index]

    def get_column(self, index: int) -> str:
        return ''.join([row[index] for row in self._board])

    def set_row(self, index: int, new_row: str) -> None:
        self._board[index] = new_row

    def set_column(self, column_index: int, new_column: str) -> None:
        for row_index, row in enumerate(self.get_rows()):
            row = row[:column_index] + new_column[row_index] + row[column_index + 1:]
            self._board[row_index] = row

    def set_cell(self, position: (int, int), new_value: str) -> None:
        column_index, row_index = position[0], position[1]
        row = self._board[row_index]
        self._board[row_index] = row[:column_index] + new_value + row[column_index + 1:]

    def get_rows(self) -> List[str]:
        return self._board

    def get_columns(self) -> List[str]:
        columns = []
        for index in range(len(self._board[0])):
            columns.append(''.join([row[index] for row in self._board]))
        return columns

    def set_board(self, board: List[str]) -> None:
        if len(board) != len(self._board):
            raise ValueError(f"Error: supplied board has different size: {len(board)}, should be: {len(self._board)}")
        self._board = board

    def get_board(self) -> List[str]:
        return self._board

    def is_valid_three_of_same(self) -> bool:
        for row in self.get_rows() + self.get_columns():
            if '000' in row or '111' in row:
                return False
        return True

    def is_valid_empty_cells(self) -> bool:
        for row in self.get_rows() + self.get_columns():
            if ' ' in row:
                return False
        return True

    def is_valid_different_counts(self, ignore_lines_with_empty_cells=False) -> bool:
        for row in self.get_rows() + self.get_columns():
            if ignore_lines_with_empty_cells and ' ' in row:
                continue
            if row.count('0') != row.count('1'):
                return False
        return True

    def is_board_solved(self) -> bool:
        if not self.is_valid_three_of_same():
            return False
        if not self.is_valid_empty_cells():
            return False
        if not self.is_valid_different_counts():
            return False
        if len(self.get_rows()) != len(set(self.get_rows())):
            return False
        if len(self.get_columns()) != len(set(self.get_columns())):
            return False

        return True

    def get_board_status(self) -> (bool, bool):  # (filled, valid)
        filled = not self.has_empty_cells()
        # We only want to know if the board has potential, e.g. not invalid (yet)
        valid = self.is_valid_three_of_same() and self.is_valid_different_counts(ignore_lines_with_empty_cells=True)
        return filled, valid

    def find_next_unsolved_cell(self) -> (int, int):
        for row_index, row in enumerate(self.get_rows()):
            for column_index, column in enumerate(row):
                if column == ' ':
                    return column_index, row_index
        return None

    def has_empty_cells(self) -> bool:
        return self.find_next_unsolved_cell() is not None

    def __str__(self):
        return '\n'.join([row for row in self._board])
