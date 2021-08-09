import io
import sys

_INPUT = """\
100 100
100 200
100 297
0 0
"""
sys.stdin = io.StringIO(_INPUT)

def main():
    from sys import stdin
    input = stdin.readline

    while True:
        n, x = map(int,input().split())
        if n==0 and x==0:
            break

        cnt = 0
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                for k in range(j+1,n+1):
                    if (i+j+k)==x:
                        cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()
