import io
import sys

_INPUT = """\
computer
Nurtures computer scientists and highly skilled computer engineers
who will create and exploit knowledge for the new era
Provides an outstanding computer environment
END_OF_TEXT
"""
sys.stdin = io.StringIO(_INPUT)


def main():
    from sys import stdin
    input = stdin.readline

    W = input().rstrip()
    T = [i.rstrip().split() for i in stdin.readlines()]

    cnt = 0
    for words in T:
        for word in words:
            if W == word.lower():
                cnt += 1
    
    print(cnt)

if __name__ == '__main__':
    main()