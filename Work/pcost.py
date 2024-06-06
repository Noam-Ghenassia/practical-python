# pcost.py
#
# Exercise 1.27
import csv
import sys
import fileparse

def portfolio_cost(filename):
    rows = fileparse.parse_csv(filename, types=[str, int, float])
    tot = sum([row['shares'] * row['price'] for row in rows])
    print(tot)

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    portfolio_cost(filename)

if __name__ == '__main__':
    main()