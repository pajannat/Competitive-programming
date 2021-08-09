import io
import sys

_INPUT = """\
40 42 -1
20 30 -1
0 2 -1
-1 -1 -1
"""
sys.stdin = io.StringIO(_INPUT)

def main():
    from sys import stdin
    input = stdin.readline

    for _ in range(50):
        m, f, r = map(int,input().split())
        if m==-1 and f==-1 and r==-1:
            break
        elif m==-1 or f==-1:
            print("F")
        elif m+f >= 80:
            print("A")
        elif m+f >= 65:
            print("B")
        elif m+f >= 50:
            print("C")
        elif m+f >= 30:
            if r >= 50:
                print("C")
            else:
                print("D")
        else:
            print("F")

if __name__ == '__main__':
    main()







