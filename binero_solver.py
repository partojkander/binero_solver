class BineroSolver:

    board = ['0010',
             '0001',
             '1001',
             '0110']

    def print_board(self):
        print('\n'.join([row for row in self.board]))

    def get_row(self, index) -> str:
        return self.board[index]

    def get_column(self, index) -> str:
        return ''.join([row[index] for row in self.board])

    @staticmethod
    def is_valid_sequence(sequence: str) -> bool:
        print(f"Validating sequence '{sequence}'")
        if '000' in sequence:
            print(f"Err: sequence '{sequence}' contains '000'")
            return False
        if '111' in sequence:
            print(f"Err: sequence '{sequence}' contains '111'")
            return False
        if ' ' in sequence:
            print(f"Err: sequence '{sequence}' contains empty cell(s)")
            return False
        if sequence.count('0') != sequence.count('1'):
            print(f"Err: sequence '{sequence}' has different amount of 1's and 0's")
            return False

        return True


if __name__ == '__main__':
    b = BineroSolver()
    print(b.is_valid_sequence(b.get_row(1)))
