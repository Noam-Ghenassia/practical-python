# report.py
#
# Exercise 2.4
import sys
from pprint import pprint
import csv


def read_portfolio(filename: str):
    with open(filename, 'rt') as f:
        headers = next(f).split(',')
        rows = [tuple(row.split(',')) for row in f]
        #rows = [(row[0], int(row[1]), float(row[2])) for row in rows]
        rows = [{'name' : row[0], 'shares' : int(row[1]), 'price' : float(row[2])} for row in rows]
    return (headers, rows)

def portfolio_cost(filename: str) -> float:
    _, rows = read_portfolio(filename)
    #tot = sum([shares * price for (_, shares, price) in rows])
    tot = sum([row['shares'] * row['price'] for row in rows])
    return(tot)

def read_prices(filename: str) -> dict:
    with open(filename, 'rt') as f:
        # prices = {row.split(',')[0] : row.split(',')[1] for row in f if len(row.split(',')) == 2}
        f_ = csv.reader(f)
        prices = {}
        for (row_num, row) in enumerate(f_):
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print(f'incorrect data format at line {row_num}')
    return prices

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    
    portfolio_filename = 'Data/portfolio.csv'
    prices_filename = 'Data/prices.csv'

    _, rows = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    margins = [row['shares'] * (row['price'] - prices[row['name'][1:-1]]) for row in rows]
    print(sum(margins))

if __name__ == '__main__':
    main()
