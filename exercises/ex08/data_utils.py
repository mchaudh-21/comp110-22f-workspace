"""Dictionary related utility functions."""

__author__ = "730550997"


from csv import DictReader

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read rows of CSV into a table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    
    # Read data as a csv, not just strings. 
    csv_reader = DictReader(file_handle)
    # Read every row line by line.
    for row in csv_reader:
        result.append(row)
    
    # Close file.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single columns."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Makes a row-oriented table into a column oriented one."""
    result: dict[str, str] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Make a new column based table using only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    if n >= len(table):
        return table

    for column in table.keys():
        n_vals = []
        for value in range(0, n):
            n_vals.append(table[column][value])
        result[column] = n_vals
    
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Make a new column based table that has on a specific subset of the original columns."""
    result: dict[str, list[str]] = {}

    for column in names:
        vals = table[column]
        result[column] = vals
    
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Make a new column based table by combining two column based tables."""
    result: dict[str, list[str]] = {}

    for column in table1.keys():
        value = table1[column]
        result[column] = value

    for column in table2.keys():
        value = table2[column]
        if column in result.keys():
            for item in value:
                result[column].append(item)
        else:
            result[column] = value
    
    return result


def count(frequency_vals: list[str]) -> dict[str, int]:
    """Make a dictionary where each key is a unique value in the inputted list and the associated value is the frequency of that value in the list."""
    result: dict[str, int] = {}
    for value in frequency_vals:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    
    return result