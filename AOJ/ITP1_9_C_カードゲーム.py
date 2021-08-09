import io
import sys

_INPUT = """\
4
a x
a x
x a
a a
"""
sys.stdin = io.StringIO(_INPUT)


def main():
    from sys import stdin
    input = stdin.readline
    N = int(input())

    # 複数行読み込み
    A = [i.rstrip().split() for i in stdin.readlines()]

    score_Taro = 0
    score_Hanako = 0
    for idx in range(N):
        if A[idx][0] > A[idx][1]:
            score_Taro += 3
        elif A[idx][0] == A[idx][1]:
            score_Taro += 1
            score_Hanako += 1
        else:
            score_Hanako += 3
    
    print(score_Taro,score_Hanako)

if __name__ == '__main__':
    main()