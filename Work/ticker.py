import csv

from follow import follow
import report
import tableformat

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def ticker(portfile, logfile, fmt):
    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    # rows = filter_symbols(rows, portfolio)
    rows = (row for row in rows if row['name'] in portfolio)
    formatter = tableformat.read_formatter(fmt)
    formatter.headings(['name', 'price', 'change'])
    for row in rows:
        formatter.row(row.values())


def main():
    ticker('Data/portfolio.csv', 'Data/stocklog.csv', fmt='txt')

if __name__ == '__main__':
    main()