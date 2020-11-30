import io
import csv
import unittest
from imcsv.imcsv import generate_temp_csvfile
from imcsv.exceptions import InconsistentCsvDataError, EmptyHeadersError


class TestImcsvCreator(unittest.TestCase):
    def test_generate_temp_csvfile_with_valid_data(self):
        headers = [
            "Date",
            "Month",
            "Year",
            "Customer ID",
            "Item ID",
        ]
        rows = [
            [
                "5-June-2020",
                "5",
                "2020",
                "920",
                "1380",
            ],
        ]

        temp_csvfile = generate_temp_csvfile(headers, rows)
        with open(temp_csvfile.name) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.assertEqual("5-June-2020", row["Date"])
                self.assertEqual("5", row["Month"])
                self.assertEqual("2020", row["Year"])
                self.assertEqual("920", row["Customer ID"])
                self.assertEqual("1380", row["Item ID"])
        self.assertIsNotNone(temp_csvfile)

    def test_generate_temp_csvfile_with_valid_inconsistent_data(self):
        headers = [
            "Date",
            "Month",
            "Year",
        ]
        rows = [
            [
                "5-June-2020",
                "5",
                "2020",
            ],
            ["0"],
        ]

        with self.assertRaises(InconsistentCsvDataError):
            _ = generate_temp_csvfile(headers, rows)

    def test_generate_temp_csvfile_with_empty_headers(self):
        headers = None
        rows = [
            [
                "5-June-2020",
                "5",
                "2020",
            ],
        ]

        with self.assertRaises(EmptyHeadersError):
            _ = generate_temp_csvfile(headers, rows)


if __name__ == "__main__":
    unittest.main()
