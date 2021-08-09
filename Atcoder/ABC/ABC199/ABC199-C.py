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
    N = int(input())
    S = list(input().split())
    S = list(S[0])
    Q = int(input())
    INPUT = [i.rstrip() for i in stdin.readlines()]

    inv_flg = 0
    for Q_list in INPUT:
        T,A,B = map(int,Q_list.split())
        if T == 1:
            if inv_flg == 0:
                S[A-1],S[B-1] = S[B-1],S[A-1]
            elif inv_flg ==1:
                S[A-1-N],S[B-1-N] = S[B-1-N],S[A-1-N]
        elif T == 2:
            if inv_flg == 0:
                inv_flg = 1
            elif inv_flg == 1:
                inv_flg = 0

    if inv_flg == 1:
        S[0:N],S[N:] = S[N:],S[0:N]

    S = ''.join(S)
    print(S)

if __name__ == '__main__':
    main()