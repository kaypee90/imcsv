# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""

    pass


class EmptyHeadersError(Error):
    """ Raised when no headers are provided """

    pass


class EmptyCsvDataError(Error):
    """
    Raised when trying to perform operation
    that requires CSV data but a null or empty
    data is provided
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

    def __init__(self, headers, row_record):
        self.message = f"Expected a list with {len(headers)} items as header but got {len(row_record)}"
        super().__init__(self.message)

    def __str__(self):
        return self.message
