def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    L_idx = 0
    R_idx = N-1
    mid_idx = (L_idx + R_idx) // 2

    # 処理
    while True:
        if A[mid_idx] < X:
            L_idx = mid_idx + 1
            mid_idx = mid_idx = (L_idx + R_idx) // 2
        elif A[mid_idx] == X:
            break
        elif X < A[mid_idx]:
            R_idx = mid_idx - 1
            mid_idx = mid_idx = (L_idx + R_idx) // 2

    
    # 答えを出力
    print(mid_idx + 1)


if __name__ == '__main__':
    main()