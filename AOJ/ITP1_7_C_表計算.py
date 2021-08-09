import io
import sys

_INPUT = """\
4 5
1 1 3 4 5
2 2 2 4 5
3 3 0 1 1
2 3 4 4 6
"""
sys.stdin = io.StringIO(_INPUT)


def main():
    from sys import stdin
    input = stdin.readline
    r, c = map(int,input().split())

    # r×c行列の入力を2次元リストに格納
    INPUT = [[]*(c) for _ in range((r))]
    for idx in range(r):
        INPUT[idx] = [int(i) for i in input().split()]

    # (r+1)×(c+1)リスト作成
    A = [[0]*(c+1) for _ in range((r+1))]

    # (r+1)×(c+1)リストに入力行列を格納
    for idx in range(r):
        for idx2 in range(c):
            A[idx][idx2] = INPUT[idx][idx2]
    
    # 各行の合計値をc+1列目に格納
    for idx in range(r):
        sum = 0
        for idx2 in range(c):
            sum += INPUT[idx][idx2]
        A[idx][c] = sum

    # 各列の合計値をr+1列目に格納
    for idx in range(c):
        sum = 0
        for idx2 in range(r):
            sum += INPUT[idx2][idx]
        A[r][idx] = sum

    # 行列の合計値を格納
    sum = 0
    for idx in range(c+1):
        sum += A[r][idx]
    A[r][c] = sum

    # 結果を出力
    for idx in range(r+1):
        for idx2 in range(c+1):
            if idx2 != c:
                print(A[idx][idx2],end=" ")
            else:
                print(A[idx][idx2])

if __name__ == '__main__':
    main()