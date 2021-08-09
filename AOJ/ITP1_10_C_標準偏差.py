import io
import sys

_INPUT = """\
5
70 80 100 90 20
3
80 80 80
0
"""
sys.stdin = io.StringIO(_INPUT)


def main():
    from sys import stdin
    input = stdin.readline
    import math

    while True:
        N = int(input())
        if N == 0:
            break

        S_list = [int(i) for i in input().split()]
        avg = sum(S_list)/len(S_list)
        std = 0
        for s in S_list:
            std += (s-avg)**2
        std /= len(S_list)
        std = math.sqrt(std)

        print(std)

if __name__ == '__main__':
    main()