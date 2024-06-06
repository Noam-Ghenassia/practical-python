from pprint import pprint
from fileparse import parse_csv

def main():
    # if len(sys.argv) == 2:
    #     filename = sys.argv[1]
    # else:
    #     filename = 'Data/portfolio.csv'
    
    portfolio_filename = '/home/noam/Documents/projects/practical-python/Work/Data/prices.csv'

    rows = parse_csv(portfolio_filename, types=[str, float], has_headers=False)
    pprint(rows)


if __name__ == '__main__':
    main()