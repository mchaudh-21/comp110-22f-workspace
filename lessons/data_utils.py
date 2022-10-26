from csv import DictReader

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


def column_values(table: list[dict[str,str]], column: str) -> list[str]:
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