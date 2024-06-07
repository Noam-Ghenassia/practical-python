from abc import ABC, abstractmethod

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
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

def read_formatter(format: str) -> TableFormatter:

    formatters = {
        "txt": TextTableFormatter(),
        "csv": CSVTableFormatter()
    }

    if format in formatters:
        return formatters[format]
    print(f"Unknown format : {format}.")