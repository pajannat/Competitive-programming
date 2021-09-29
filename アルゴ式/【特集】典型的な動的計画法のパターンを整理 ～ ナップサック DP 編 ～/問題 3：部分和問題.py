def main():
    from sys import stdin
    input = stdin.readline

    # サイズを取得
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # N × M の配列を用意する
    # 配列全体を 0 に初期化しておく
    dp = [[0]*(M+1) for _ in range(N+1)]

    # dp[0][0]に初期値を設定
    dp[0][0] = 1

    # 0, 1, 2, ..., N 行目を順に計算していく
    for i in range(N):
        # 0, 1, 2, ..., M 列目を順に計算していく
        for j in range(M+1):
            # dp[i][j]に移動済みの場合(初期値0以外が入っている)
            if dp[i][j] == 1:
                # 下に配る
                dp[i+1][j] = 1
                # 右下に配る
                if j+A[i] <= M:
                    dp[i+1][j+A[i]] = 1

    # 右下のマスに到達dp[-1][-1]=1していたらYesを出力。
    if dp[-1][-1] ==1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()