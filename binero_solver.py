from copy import deepcopy

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

    def apply_solutions(self) -> None:
        while True:
            old_board = deepcopy(self.board.get_board())
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

    def brute_force(self, board_: BineroBoard) -> BineroBoard or None:
        board = deepcopy(board_)
        # board_str = str(board).replace('\n', ', ')
        # print(f"brute_force(), board is: '{board_str}'")

        filled, valid = board_.get_board_status()
        if filled:
            if board.is_board_solved():
                # Board is solved, return it
                return board
            else:
                return None
        if not valid:
            return None
        else:
            # Board is not filled but yet valid
            next_unsolved_cell = board.find_next_unsolved_cell()
            board.set_cell(next_unsolved_cell, "0")
            new_board = self.brute_force(board)
            if new_board is not None:
                return new_board
            else:
                board.set_cell(next_unsolved_cell, "1")
                return self.brute_force(board)
