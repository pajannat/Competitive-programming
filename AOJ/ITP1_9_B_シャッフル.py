import io
import sys

_INPUT = """\
aabc
3
1
2
1
vwxyz
2
3
4
-
"""
sys.stdin = io.StringIO(_INPUT)

def main():
    from sys import stdin
    input = stdin.readline
    while True:
        S = input().rstrip()
        if S == "-":
            break
        m = int(input())
        h = [0]*m
        for i in range(m):
            h[i] = int(input())
        
        for idx in range(m):
            S = S[h[idx]:] + S[0:h[idx]]

        print(S)

if __name__ == '__main__':
    main()