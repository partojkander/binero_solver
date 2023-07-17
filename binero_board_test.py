import unittest

from hamcrest import assert_that, equal_to

from binero_board import BineroBoard


class BineroBoardTest(unittest.TestCase):

    def test_get_row(self):
        board = ['01',
                 '10']
        b = BineroBoard()
        b.board = board
        assert_that(b.get_row(0), equal_to('01'))
        assert_that(b.get_row(1), equal_to('10'))

    def test_get_column(self):
        board = ['10',
                 '10']
        b = BineroBoard()
        b.board = board
        assert_that(b.get_column(0), equal_to('11'))
        assert_that(b.get_column(1), equal_to('00'))

    def test_valid_sequence(self):
        board = BineroBoard()
        assert_that(board.is_valid_sequence('010101'), equal_to(True))

    def test_invalid_sequence_three_zeroes(self):
        binero_board = BineroBoard()
        assert_that(binero_board.is_valid_sequence('11000110'), equal_to(False))

    def test_invalid_sequence_three_ones(self):
        binero_board = BineroBoard()
        assert_that(binero_board.is_valid_sequence('11100110'), equal_to(False))

    def test_invalid_sequence_mismatching_counts(self):
        binero_board = BineroBoard()
        assert_that(binero_board.is_valid_sequence('1011'), equal_to(False))

    def test_invalid_sequence_empty_cells(self):
        binero_board = BineroBoard()
        assert_that(binero_board.is_valid_sequence('1 010'), equal_to(False))

    def test_board_is_solved(self):
        binero_board = BineroBoard()
        binero_board.board = ['0110',
                              '1001',
                              '1001',
                              '0110']
        assert_that(binero_board.is_board_solved(), equal_to(True))