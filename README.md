imcsv - Fast Python In-Memory CSV file creator!
---------------------------------------------------------

An in-memory CSV generator. The library is built to enhance test cases that require csv files.

Requirements
------------

* **Python**:  3.*


Installation
------------

Install using pip:

    pip install imcsv

Usage
-----

Provides you with an in-memory csv file


    from imcsv.imcsv import generate_temp_csvfile

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
        [
            "4-December-2020",
            "12",
            "2020",
            "977",
            "2322",
        ],
    ]
	temp_csvfile = generate_temp_csvfile(headers, rows)
