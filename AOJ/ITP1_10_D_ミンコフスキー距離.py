import io
import sys

_INPUT = """\
3
1 2 3
2 0 4
"""
sys.stdin = io.StringIO(_INPUT)

def main():
    from sys import stdin
    input = stdin.readline
    N = int(input())
    x_lst = [int(i) for i in input().split()]
    y_lst = [int(i) for i in input().split()]
    abs_lst = [abs(x_lst[idx]-y_lst[idx]) for idx in range(N)]

    for p in range(1,4):
        sum = 0
        for num in abs_lst:
            sum = sum + num**p
        D = sum**(1/p)
        print(D)

    print(max(abs_lst))

if __name__ == '__main__':
    main()