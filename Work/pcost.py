# pcost.py
#
# Exercise 1.27
import csv
import sys

"""def extract(filename):
    with open(filename, 'rt') as f:
        headers = next(f).split(',')
        rows = [row.split(',') for row in f]
    return (headers, rows)"""

def extract(filename):
    with open(filename, 'rt') as f:
        r = csv.reader(f)
        headers = next(r)
        rows = list(r)
    return (headers, rows)

def portfolio_cost(filename):
    _, rows = extract(filename)
    #tot = sum([int(row[1]) * float(row[2]) for row in rows])
    tot=0
    for row in rows :
        try:
            tot += int(row[1]) * float(row[2])
        except ValueError:
            print('missing data')
    print(tot)

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    portfolio_cost(filename)

if __name__ == '__main__':
    main()