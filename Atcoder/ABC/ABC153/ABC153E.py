def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    H, N = map(int, input().split())
    A = []
    B = []

    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # H+1 の配列を用意する
    # 配列全体を inf で初期化する
    inf = 10**8 + 5
    dp = [inf] * (H+1)

    # 初期状態
    # モンスターのHPがH時点では、魔力の消費 0
    dp[H] = 0

    # 魔法を順に考慮していく
    for i in range(N):
        # モンスターのHPが j 時点で魔法を使用することを考える
        # 各魔法を組み合わせても到達できないHP j は魔力消費 inf となる
        # これにより到達の可不可が考慮されている
        for j in range(H, -1, -1):

            # i 番目の魔法を使用する場合 (A[i] 個 左のマスへ進む場合)
            # (モンスターのHPが負となった場合はHP 0 として扱う)
            dp[max(0, j - A[i])] = min(dp[max(0, j - A[i])], dp[j] + B[i])

    # 答え
    print(dp[0])


if __name__ == '__main__':
    main()