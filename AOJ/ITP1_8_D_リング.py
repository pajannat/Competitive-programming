import io
import sys

_INPUT = """\
vanceknowledgetoad
advance
"""
sys.stdin = io.StringIO(_INPUT)

def main():
    from sys import stdin
    input = stdin.readline

    S = input().rstrip()
    P = input().rstrip()

    SS = S+S

    if P in SS:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()