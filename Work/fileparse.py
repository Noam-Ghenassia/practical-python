# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename: str,
              select = None,
              types = None,
              has_headers=True,
              delimiter=',',
              silence_errors=False) -> list:
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")
    
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        if has_headers:
            headers = next(rows)
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select

            records = []
            for row_num, row in enumerate(rows):
                if not row:    # Skip rows with no data
                    continue
                if select:
                    row = [row[index] for index in indices]
                if types:
                    try:
                        row = [t(item) for item, t in zip(row, types)]
                    except TypeError as e:
                        if not silence_errors:
                            print(f"row {row_num} : {row} couldn't be converted : ", e)
                record = dict(zip(headers, row))
                records.append(record)
        
        else:
            records = []
            for row in rows:
                if row:
                    records.append(tuple(t(item) for item, t in zip(row, types)))

    return records