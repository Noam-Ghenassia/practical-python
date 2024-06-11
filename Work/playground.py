from pprint import pprint
from typing import Iterable

class Test:
    def __init__(self, ls):
        self.ls = ls
    
    def __iter__(self):
        return self.ls.__iter__()

def foo(ls: Iterable) -> None:
    for l in ls:
        print("test")

def main():
    # if len(sys.argv) == 2:
    #     filename = sys.argv[1]
    # else:
    #     filename = 'Data/portfolio.csv'
    t = Test([1, 2, 3, 4])
    print([r for r in t])

    foo(t)

    print(Test.__bases__)

    print(isinstance(t, Iterable))


if __name__ == '__main__':
    main()