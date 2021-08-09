import io
import sys

_INPUT = """\
100 50 4

"""
sys.stdin = io.StringIO(_INPUT)


#------以下にコードを記述-----
def main():
    from sys import stdin
    input = stdin.readline
    A,B,C = map(int,input().split())
    if A*A+B*B < C*C:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()