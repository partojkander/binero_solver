import unittest

from hamcrest import assert_that, equal_to, not_

from binero_solver import BineroSolver


class TestBineroSolver(unittest.TestCase):

    def test_fill_around_doubles(self):
        solver = BineroSolver(size=4)
        assert_that(solver.fill_around_double('00 '), equal_to('001'))
        assert_that(solver.fill_around_double(' 00'), equal_to('100'))
        assert_that(solver.fill_around_double('11 '), equal_to('110'))
        assert_that(solver.fill_around_double(' 11'), equal_to('011'))

        assert_that(solver.fill_around_double('1 '), equal_to('1 '))
        assert_that(solver.fill_around_double('11001 0 1'), equal_to('11001 0 1'))

    def test_fill_gaps(self):
        solver = BineroSolver(size=10)
        assert_that(solver.fill_gap(' 0 0   0 0'), equal_to(' 010   010'))
        assert_that(solver.fill_gap(' 1 1   1 1'), equal_to(' 101   101'))

        assert_that(solver.fill_gap('010 101'), equal_to('010 101'))

    def test_solve_doubles(self):
        solver = BineroSolver(size=4)
        solver.board.set_board(['    ',
                                ' 00 ',
                                ' 00 ',
                                '    '])
        solver.apply_solutions()
        expected_board = ['0110',
                          '1001',
                          '1001',
                          '0110']
        assert_that(solver.board.get_board(), equal_to(expected_board))

    def test_solve_gaps(self):
        solver = BineroSolver(size=4)
        solver.board.set_board([' 0 0',
                                '1   ',
                                ' 1 1',
                                '1   '])
        solver.apply_solutions()
        expected_board = [' 010',
                          '1   ',
                          '0101',
                          '1   ']
        assert_that(solver.board.get_board(), equal_to(expected_board))

    def test_brute_force_1(self):
        solver = BineroSolver(size=2)
        solver.board.set_board(['10',
                                '  '])
        solved_board = solver.brute_force(solver.board)
        assert_that(solved_board.get_board(), equal_to(['10', '01']))

    def test_brute_force_2(self):
        solver = BineroSolver(size=4)
        solved_board = solver.brute_force(solver.board)
        print(solved_board)
        assert_that(solved_board, not_(equal_to(None)))
        assert_that(solved_board.is_board_solved(), equal_to(True))
