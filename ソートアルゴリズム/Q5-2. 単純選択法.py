def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))

    for i in range(N-1):
        # A[i]より小さい値を一周探索
        min_idx = i
        for j in range(i+1, N):
            if A[min_idx] > A[j]:
                min_idx = j
        # 一周探索後、A[i]より小さい値が見つかった場合は
        # A[i], A[min_idx]を入れ替え
        if min_idx != i:
            A[i], A[min_idx] = A[min_idx], A[i]
        # ソート過程を出力
        print(*A)

if __name__ == '__main__':
    main()