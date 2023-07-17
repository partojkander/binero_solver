class BineroInvalidSequenceException(Exception):
    pass


class BineroThreeZeroesException(BineroInvalidSequenceException):
    pass


class BineroThreeOnesException(BineroInvalidSequenceException):
    pass


class BineroMismatchingCountException(BineroInvalidSequenceException):
    pass


class BineroEmptyCellsException(BineroInvalidSequenceException):
    pass
