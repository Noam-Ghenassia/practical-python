# report.py
#
# Exercise 2.4

# import sys
from functools import reduce
from pprint import pprint
import csv


def read_portfolio(filename: str):
    with open(filename, 'rt') as f:
        headers = next(f).split(',')
        rows = [tuple(row.split(',')) for row in f]
        #rows = [(row[0], int(row[1]), float(row[2])) for row in rows]
        rows = [{'name' : row[0][1:-1], 'shares' : int(row[1]), 'price' : float(row[2])} for row in rows]
    return (headers, rows)

def portfolio_cost(filename: str) -> float:
    _, rows = read_portfolio(filename)
    #tot = sum([shares * price for (_, shares, price) in rows])
    tot = sum([row['shares'] * row['price'] for row in rows])
    return(tot)

def read_prices(filename: str) -> dict:
    with open(filename, 'rt') as f:
        # prices = {row.split(',')[0][1:-1] : float(row.split(',')[1]) for row in f if len(row.split(',')) == 2}
        f_ = csv.reader(f)
        prices = {}
        for (row_num, row) in enumerate(f_):
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print(f'incorrect data format at line {row_num}')
    return prices

def compute_margin(portfolio_filename: str, prices_filename: str) -> float:
    _, rows = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    margins = [row['shares'] * (row['price'] - prices[row['name']]) for row in rows]
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


def main():
    # if len(sys.argv) == 2:
    #     filename = sys.argv[1]
    # else:
    #     filename = 'Data/portfolio.csv'
    
    portfolio_filename = '/home/noam/Documents/projects/practical-python/Work/Data/portfolio.csv'
    prices_filename = '/home/noam/Documents/projects/practical-python/Work/Data/prices.csv'

    report = make_report(portfolio_filename, prices_filename)
    headers = ('Name', 'Shares', 'Price', 'Change')
    headers_line = reduce(lambda a, b: a+f"{b:>10s}", list(headers), " ")
    print(headers_line)
    print("-"*len(headers_line))
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')



if __name__ == '__main__':
    main()
