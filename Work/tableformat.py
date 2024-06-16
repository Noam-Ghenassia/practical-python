from abc import ABC, abstractmethod
from collections import Iterable
from typing import List

class TableFormatter(ABC):

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class FormatError(Exception):
    pass

def read_formatter(format: str) -> TableFormatter:

    formatters = {
        "txt": TextTableFormatter(),
        "csv": CSVTableFormatter()
    }

    if format in formatters:
        return formatters[format]
    raise FormatError(f"Unknown format : {format}.")

def print_table(rows: Iterable, col_names: List[str], formatter: TableFormatter):
    formatter.headings(col_names)
    for row in rows:
        formatter.row([getattr(row, col_name) for col_name in col_names])
