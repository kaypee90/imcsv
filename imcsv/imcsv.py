import csv
import tempfile
from imcsv.exceptions import (
    EmptyHeadersError,
    NullCsvFileError,
    NullCsvFileError,
    InconsistentCsvDataError,
)


def _generate_csv_data(headers: list, data: list):
    """
    Utility function for generating the mapped
    data dictionary for creating csv records
    :param
        headers: list
            A list of file headers where each item is a string
        data: list
            A list containing another list representing the row and column for the CSV
    :returns: list
        csv_records :
            A list object containing dictionaries which map records to their corresponding headers
    """
    records = []
    if not headers:
        raise EmptyHeadersError

    if not data:
        raise EmptyCsvDataError

    for row_record in data:
        if len(headers) != len(row_record):
            raise InconsistentCsvDataError(headers, row_record)
        record = dict(zip(headers, row_record))
        records.append(record)
    return records


def _write_data_to_csv(csvfile: object, headers: list, data: list = None):
    """
    Utility function for writing data to an in-memory csv file
    :param
        csvfile: IO
            An in-memory temporary csv file
        headers: list
            A list of file headers where each item is a string
        data: list
            A list containing another list representing the row and column for the CSV
    """
    if not csvfile:
        raise NullCsvFileError

    if not headers:
        raise EmptyHeadersError

    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    if data:
        csv_records = _generate_csv_data(headers, data)
        for record in csv_records:
            writer.writerow(record)


def generate_temp_csvfile(headers: list, data: list) -> object:
    """
    Generates in-memory csv files
    :param
        headers: list
            A list of file headers where each item is a string
        data: list
            A list containing another list representing the rows for the CSV
    :returns: IO
        csvfile :
            In-memory temporary csv file
    """
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as csvfile:
        _write_data_to_csv(csvfile, headers, data)

    return csvfile
