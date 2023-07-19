import unittest

from hamcrest import assert_that, equal_to, raises, calling

from binero_board import BineroBoard
from exceptions import (
    BineroEmptyCellsException,
    BineroMismatchingCountException,
    BineroThreeOnesException,
    BineroThreeZeroesException
)


class TestBineroBoard(unittest.TestCase):

    def test_get_row(self):
        board = ['01',
                 '10']
        b = BineroBoard()
        b.board = board
        assert_that(b.get_row(0), equal_to('01'))
        assert_that(b.get_row(1), equal_to('10'))

    def test_get_column(self):
        board = ['1010',
                 '1001',
                 '0110',
                 '0011']
        b = BineroBoard()
        b.board = board
        assert_that(b.get_column(0), equal_to('1100'))
        assert_that(b.get_column(1), equal_to('0010'))
        assert_that(b.get_column(2), equal_to('1011'))
        assert_that(b.get_column(3), equal_to('0101'))

    def test_valid_sequence(self):
        board = BineroBoard()
        assert_that(board.is_valid_sequence('010101'), equal_to(True))

    def test_invalid_sequence_three_zeroes(self):
        binero_board = BineroBoard()
        assert_that(calling(binero_board.is_valid_sequence).with_args('11000110'),
                    raises(BineroThreeZeroesException))

    def test_invalid_sequence_three_ones(self):
        binero_board = BineroBoard()
        assert_that(calling(binero_board.is_valid_sequence).with_args('11100110'),
                    raises(BineroThreeOnesException))

    def test_invalid_sequence_mismatching_counts(self):
        binero_board = BineroBoard()
        assert_that(calling(binero_board.is_valid_sequence).with_args('1011'),
                    raises(BineroMismatchingCountException))

    def test_invalid_sequence_empty_cells(self):
        binero_board = BineroBoard()
        assert_that(calling(binero_board.is_valid_sequence).with_args('1 010'),
                    raises(BineroEmptyCellsException))

    def test_board_is_solved(self):
        binero_board = BineroBoard()
        binero_board.board = ['0101',
                              '1010',
                              '1100',
                              '0011']
        assert_that(binero_board.is_board_solved(), equal_to(True))

    def test_set_row(self):
        binero_board = BineroBoard()
        binero_board.board = ['  ',
                              '11']
        binero_board.set_row(0, '00')
        assert_that(binero_board.board, equal_to(['00', '11']))

    def test_set_column_1(self):
        binero_board = BineroBoard()
        binero_board.board = ['1 ',
                              '1 ']
        binero_board.set_column(1, '00')
        assert_that(binero_board.board, equal_to(['10', '10']))

    def test_set_column_2(self):
        binero_board = BineroBoard()
        binero_board.board = ['0000',
                              '0000',
                              '0000',
                              '0000']
        binero_board.set_column(2, '1010')
        expected_board = ['0010',
                          '0000',
                          '0010',
                          '0000']
        assert_that(binero_board.board, equal_to(expected_board))
