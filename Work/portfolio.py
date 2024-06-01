def main():
    with open('Data/portfolio.csv', 'rt') as f:
        headers = next(f).split(',')
        rows = [row.split(',') for row in f]
        print(headers)
        print(rows)


if __name__ == '__main__':
    main()