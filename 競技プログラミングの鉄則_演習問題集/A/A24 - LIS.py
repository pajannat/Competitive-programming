def main():
    from sys import stdin
    input = stdin.readline

    import bisect

    # 入力を受け取る
    N = int(input())
    A = [0] + list(map(int, input().split()))

    # dp[i] -> A[i]を末尾とする最長の部分列の長さ
    dp = [0] * (N+1)
    # L[i] -> 長さ i のLISの末尾の数値
    L = [10**6] * (N+1)

    # 処理
    # LIS
    # 初期化
    L[0] = 0
    for i in range(1, N+1):
        # L[pos - 1] < A[i] を満たす最大のpos. Lの範囲はL[0] ~ L[i-1]
        # (A[i] をどの長さのLISの末尾に付け加えられるかを探索)
        pos = bisect.bisect_left(L, A[i])
        # L[pos - 1] 末尾に A[i]を付け加えるので, dp[i] の長さは pos
        dp[i] = pos
        # 長さ pos となるLIS の末尾の数字の更新. 同じ長さのLISであれば, 末尾は小さい数字の方がよい
        L[pos] = min(L[pos], A[i])


    # 答えを出力
    print(max(dp))


if __name__ == '__main__':
    main()