import io
import sys

_INPUT = """\
3 2 3
1 2
0 3
4 5
1 2 1
0 3 2
"""
sys.stdin = io.StringIO(_INPUT)

def main():
    from sys import stdin
    input = stdin.readline
    n, m, l = map(int,input().split())

    # n×m行列の入力を2次元リストに格納
    A = [[]*(m) for _ in range(n)]
    for idx in range(n):
        A[idx] = [int(i) for i in input().split()]

    # m×l行列の入力を2次元リストに格納
    B = [[]*(l) for _ in range(m)]
    for idx in range(m):
        B[idx] = [int(i) for i in input().split()]

    # n×lリスト作成
    C = [[0]*l for _ in range(n)]

    # 行列積計算(A*B)
    for idx_n in range(n):
        for idx_l in range(l):
            sum = 0
            for idx_m in range(m):
                sum += A[idx_n][idx_m]*B[idx_m][idx_l]
            C[idx_n][idx_l] = sum

    # 結果を出力
    for idx_n in range(n):
        for idx_l in range(l):
            if idx_l == l-1:
                print(C[idx_n][idx_l])
            else:
                print(C[idx_n][idx_l],end=" ")

if __name__ == '__main__':
    main()