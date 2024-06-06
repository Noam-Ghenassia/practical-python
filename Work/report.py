# report.py
#
# Exercise 2.4

import sys
from functools import reduce
from pprint import pprint
import csv

import fileparse

def read_prices(filename: str) -> dict:
    prices = fileparse.parse_csv(filename, types=[str, float], has_headers=False)
    return {price[0] : price[1] for price in prices}

def compute_margin(portfolio_filename: str, prices_filename: str) -> float:
    rows = fileparse.parse_csv(portfolio_filename, types=[str, int, float])
    prices = read_prices(prices_filename)
    margins = [row['shares'] * (prices[row['name']] - row['price']) for row in rows]
    print(sum(margins))

def make_report(portfolio_filename: str, prices_filename: str) -> None:
    p_rows = fileparse.parse_csv(portfolio_filename, types=[str, int, float])
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
    #headers_line = reduce(lambda a, b: a+f"{b:>10s}", list(headers), " ")
    headers_line = '%10s %10s %10s %10s'  % headers
    print(headers_line)
    print("-"*len(headers_line))
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

def main(args):
    portfolio_filename = args[0]
    prices_filename = args[1]
    print_report(portfolio_filename, prices_filename)



if __name__ == '__main__':
    if len(sys.argv) == 3:
        portfolio_filename = sys.args[1]
        prices_filename = sys.args[2]
    else:
        portfolio_filename = '/home/noam/Documents/projects/practical-python/Work/Data/portfolio.csv'
        prices_filename = '/home/noam/Documents/projects/practical-python/Work/Data/prices.csv'

    main([portfolio_filename, prices_filename])
