# report.py
#
# Exercise 2.4

# import sys
from functools import reduce
from pprint import pprint
import csv


def read_portfolio(filename: str):
    with open(filename, 'rt') as f:
        headers = next(f).rstrip().split(',')
        rows = []
        for row_num, row in enumerate(f):
            if "" in row.rstrip().split(',') or '' in row.rstrip().split(','):
                print(f"incorrect data format in file {filename} at line {row_num}")
            else:
                rows.append(dict(zip(headers, row.rstrip().split(','))))

    for row_num, row in enumerate(rows):
        row['name'] = row['name'][1:-1]
        row['shares'] = int(row['shares'])
        row['price'] = float(row['price'])
    return (headers, rows)

def portfolio_cost(filename: str) -> float:
    _, rows = read_portfolio(filename)
    tot = sum([row['shares'] * row['price'] for row in rows])
    return(tot)

def read_prices(filename: str) -> dict:
    with open(filename, 'rt') as f:
        f_ = csv.reader(f)
        prices = {}
        for (row_num, row) in enumerate(f_):
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print(f'incorrect data format in file {filename} at line {row_num}')
    return prices

def compute_margin(portfolio_filename: str, prices_filename: str) -> float:
    _, rows = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    margins = [row['shares'] * (prices[row['name']] - row['price']) for row in rows]
    print(sum(margins))

def make_report(portfolio_filename: str, prices_filename: str) -> None:
    _, p_rows = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    rows = []
    for p_row in p_rows:
        name, shares = p_row['name'], p_row['shares']
        price = prices[p_row['name']]
        change = price - p_row['price']
        rows.append((name, shares, price, change))
    return rows

def print_report(portfolio_filename: str, prices_filename: str) -> None:
    report = make_report(portfolio_filename, prices_filename)
    headers = ('Name', 'Shares', 'Price', 'Change')
    headers_line = reduce(lambda a, b: a+f"{b:>10s}", list(headers), " ")
    print(headers_line)
    print("-"*len(headers_line))
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

def main():
    # if len(sys.argv) == 2:
    #     filename = sys.argv[1]
    # else:
    #     filename = 'Data/portfolio.csv'
    
    portfolio_filename = '/home/noam/Documents/projects/practical-python/Work/Data/portfoliodate.csv'
    prices_filename = '/home/noam/Documents/projects/practical-python/Work/Data/prices.csv'

    print_report(portfolio_filename, prices_filename)



if __name__ == '__main__':
    main()
