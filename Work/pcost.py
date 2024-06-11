# pcost.py
#
# Exercise 1.27
import csv
import sys


import fileparse
import report

# def portfolio_cost(filename):
#     rows = fileparse.parse_csv(filename, types=[str, int, float])
#     tot = sum([row['shares'] * row['price'] for row in rows])
#     print(tot)

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    print(portfolio_cost(filename))

if __name__ == '__main__':
    main()