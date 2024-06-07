# report.py
#
# Exercise 2.4

import sys
from functools import reduce
from pprint import pprint
import csv

import fileparse
import stock
import tableformat

def read_prices(filename: str) -> dict:
    prices = fileparse.parse_csv(filename, types=[str, float], has_headers=False)
    return {price[0] : price[1] for price in prices}

def read_portfolio(filename: str) -> list:
    rows = fileparse.parse_csv(filename, types=[str, int, float])
    return [stock.Stock(row['name'], row['shares'], row['price']) for row in rows]

def compute_margin(portfolio_filename: str, prices_filename: str) -> float:
    rows = fileparse.parse_csv(portfolio_filename, types=[str, int, float])
    prices = read_prices(prices_filename)
    margins = [row['shares'] * (prices[row['name']] - row['price']) for row in rows]
    print(sum(margins))

def make_report(portfolio_filename: str, prices_filename: str) -> None:
    stocks = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    rows = []
    for stock in stocks:
        name, shares = stock.name, stock.shares
        price = prices[stock.name]
        change = price - stock.price
        rows.append((name, shares, price, change))
    return rows

# def print_report(portfolio_filename: str, prices_filename: str, formatter: TableFormatter) -> None:
#     report = make_report(portfolio_filename, prices_filename)
#     headers = ('Name', 'Shares', 'Price', 'Change')
#     #headers_line = reduce(lambda a, b: a+f"{b:>10s}", list(headers), " ")
#     headers_line = '%10s %10s %10s %10s'  % headers
#     print(headers_line)
#     print("-"*len(headers_line))
#     for name, shares, price, change in report:
#         print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

def print_report(portfolio_filename: str, prices_filename: str, formatter: tableformat.TableFormatter) -> None:
    report = make_report(portfolio_filename, prices_filename)
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)




def main(args, fmt='txt'):
    portfolio_filename = args[0]
    prices_filename = args[1]
    formatter = tableformat.read_formatter(fmt)
    print_report(portfolio_filename, prices_filename, formatter)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        portfolio_filename = sys.args[1]
        prices_filename = sys.args[2]
    else:
        portfolio_filename = '/home/noam/Documents/projects/practical-python/Work/Data/portfolio.csv'
        prices_filename = '/home/noam/Documents/projects/practical-python/Work/Data/prices.csv'

    main([portfolio_filename, prices_filename])
