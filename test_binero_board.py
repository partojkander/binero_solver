import unittest

from hamcrest import assert_that, equal_to, raises, calling

from binero_board import BineroBoard


class TestBineroBoard(unittest.TestCase):

    def test_get_row(self):
        board = ['01',
                 '10']
        b = BineroBoard(size=2)
        b.set_board(board)
        assert_that(b.get_row(0), equal_to('01'))
        assert_that(b.get_row(1), equal_to('10'))

    def test_get_column(self):
        b = BineroBoard(size=4)
        b.set_board(['1010',
                     '1001',
                     '0110',
                     '0011'])
        assert_that(b.get_column(0), equal_to('1100'))
        assert_that(b.get_column(1), equal_to('0010'))
        assert_that(b.get_column(2), equal_to('1011'))
        assert_that(b.get_column(3), equal_to('0101'))

    def test_board_is_solved(self):
        binero_board = BineroBoard(size=4)
        binero_board.set_board(['0101',
                                '1010',
                                '1100',
                                '0011'])
        assert_that(binero_board.is_board_solved(), equal_to(True))

    def test_set_row(self):
        binero_board = BineroBoard(size=2)
        binero_board.set_board(['  ',
                                '11'])
        binero_board.set_row(0, '00')
        assert_that(binero_board.get_board(), equal_to(['00', '11']))

    def test_set_column_1(self):
        binero_board = BineroBoard(size=2)
        binero_board.set_board(['1 ',
                                '1 '])
        binero_board.set_column(1, '00')
        assert_that(binero_board.get_board(), equal_to(['10', '10']))

    def test_set_column_2(self):
        binero_board = BineroBoard(size=4)
        binero_board.set_board(['0000',
                                '0000',
                                '0000',
                                '0000'])
        binero_board.set_column(2, '1010')
        expected_board = ['0010',
                          '0000',
                          '0010',
                          '0000']
        assert_that(binero_board.get_board(), equal_to(expected_board))

    def test_invalid_board_size(self):
        assert_that(calling(BineroBoard).with_args(size=1), raises(ValueError))

    def test_set_board_with_invalid_size(self):
        board = BineroBoard(size=4)
        assert_that(calling(board.set_board).with_args(['10', '01']), raises(ValueError))

    def test_find_unsolved_empty_board(self):
        binero_board = BineroBoard(size=4)
        assert_that(binero_board.find_next_unsolved_cell(), equal_to((0, 0)))

    def test_find_unsolved_full_board(self):
        binero_board = BineroBoard(size=2)
        binero_board.set_board(['01',
                                '10'])
        assert_that(binero_board.find_next_unsolved_cell(), equal_to(None))

    def test_find_unsolved_partial_board(self):
        binero_board = BineroBoard(size=4)
        binero_board.set_board(['0101',
                                '1010',
                                '101 ',
                                '1001'])
        assert_that(binero_board.find_next_unsolved_cell(), equal_to((3, 2)))

    def test_set_cell(self):
        binero_board = BineroBoard(size=2)
        binero_board.set_cell((1, 1), '1')
        assert_that(binero_board.get_board(), equal_to(['  ', ' 1']))

    def test_has_empty_cells(self):
        full_board = BineroBoard(size=2)
        full_board.set_board(['01',
                              '10'])
        non_full_board = BineroBoard(size=2)
        partial_board = BineroBoard(size=2)
        partial_board.set_board([' 1',
                                 '01'])
        assert_that(full_board.has_empty_cells(), equal_to(False))
        assert_that(non_full_board.has_empty_cells(), equal_to(True))
        assert_that(partial_board.has_empty_cells(), equal_to(True))

    def test_get_board_status_1(self):
        board = BineroBoard(size=2)
        board.set_board(['01', '10'])
        assert_that(board.get_board_status(), equal_to((True, True)))

    def test_get_board_status_2(self):
        board = BineroBoard(size=2)
        board.set_board(['01', '1 '])
        assert_that(board.get_board_status(), equal_to((False, True)))

    def test_get_board_status_3(self):
        board = BineroBoard(size=4)
        board.set_board(['0111',
                         '1010',
                         '0101',
                         '011 '])
        assert_that(board.get_board_status(), equal_to((False, False)))

    def test_get_board_status_4(self):
        board = BineroBoard(size=4)
        board.set_board(['0111',
                         '1010',
                         '0101',
                         '0111'])
        assert_that(board.get_board_status(), equal_to((True, False)))

    def test_get_board_status_5(self):
        board = BineroBoard(size=4)
        board.set_board(['0010', '000 ', '    ', '    '])
        assert_that(board.get_board_status(), equal_to((False, False)))

    def test_get_board_status_6(self):
        board = BineroBoard(size=4)
        board.set_board(['0010', '0011', '    ', '    '])
        assert_that(board.get_board_status(), equal_to((False, False)))

    def test_is_valid_three_of_same(self):
        board = BineroBoard(size=4)
        board.set_board(['000 ', '    ', '    ', '    '])
        assert_that(board.is_valid_three_of_same(), equal_to(False))

        board.set_board(['111 ', '    ', '    ', '    '])
        assert_that(board.is_valid_three_of_same(), equal_to(False))

        board.set_board(['1   ', '1   ', '1   ', '    '])
        assert_that(board.is_valid_three_of_same(), equal_to(False))

    def test_is_valid_empty_cells(self):
        board = BineroBoard(size=4)
        board.set_board(['0001', '1111', '1111', '111 '])
        assert_that(board.is_valid_empty_cells(), equal_to(False))

        board.set_board(['0001', '1111', '1111', '1111'])
        assert_that(board.is_valid_empty_cells(), equal_to(True))

    def test_is_valid_different_counts(self):
        board = BineroBoard(size=2)
        board.set_board(['01', '11'])
        assert_that(board.is_valid_different_counts(), equal_to(False))

        board.set_board(['01', '10'])
        assert_that(board.is_valid_different_counts(), equal_to(True))
