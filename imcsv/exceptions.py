# define Python user-defined exceptions
"""
Package exception definitions
"""


class Error(Exception):
    """Base class for other exceptions"""

    pass


class EmptyHeadersError(Error):
    """Raised when no headers are provided"""

    pass


class NullCsvDataError(Error):
    """
    Raised when trying to perform operation
    that requires CSV data of a list type
    but null is provided
    """

    pass


class NullCsvFileError(Error):
    """
    Exception raised when temporal in-memory file is null
    """

    pass


class InconsistentCsvDataError(Error):
    """
    Exception raised when length of record in csv is not equal to
    the length of the headers list provided
    """

    def __init__(self, headers, row_record) -> None:
        self.message = f"Expected a list with {len(headers)} items as header but got {len(row_record)}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
