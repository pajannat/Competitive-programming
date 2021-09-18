def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    X, Y = map(int, input().split())
    # i種類目の弁当のたこ焼きの個数A, たい焼きの個数B
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    # dp[i] -> i種類目の弁当まで買うか買わないかを検討
    # dp[i][j][k] -> i種類目の弁当まで買うか買わないかを検討したとき、
    #                たこ焼きj個, たい焼きk個手に入れるための弁当の個数の最小値
    # 購入数の最大個数N+1で初期化
    dp = [[[N+1]*(Y+1) for _ in range(X+1)] for _ in range(N+1)]
    # 購入数i=0のとき、たこ焼きj=0個、たい焼きk=0個
    dp[0][0][0] = 0

    # 0,1,2,...,N種類目まで順に弁当の購入を検討
    for i in range(N):
        for j in range(X+1):
            for k in range(Y+1):
                # 弁当i種類目までで、たこ焼きj個、たい焼きk個が取得できている場合
                # (dp[i][j][k]の値が初期値から更新されている場合)
                if dp[i][j][k] != N+1:
                    # i種類目の弁当を購入しない場合
                    # dp[i+1][j][k]の値を更新
                    # j,kまでのループの弁当購入パターンですでに
                    # dp[i+1][j][k]が埋まっている場合がある。比較して小さい方を入力
                    dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                    # i種類目の弁当を購入した場合
                    # たこ焼きX個、たい焼きY個の上限を超える場合。
                    # dp[i+1][X][Y]の値を埋める
                    if (j+A[i] > X) and (k+B[i] > Y):
                        dp[i+1][X][Y] = min(dp[i+1][X][Y], dp[i][j][k]+1)
                    # たこ焼きX個の上限のみ超える場合。
                    # dp[i+1][X][k+B[i]]の値を埋める
                    elif (j+A[i] > X):
                        dp[i+1][X][k+B[i]] = min(dp[i+1][X][k+B[i]], dp[i][j][k]+1)
                    # たい焼きY個の上限のみ超える場合。
                    # dp[i+1][j+A[i]][Y]の値を埋める
                    elif (k+B[i] > Y):
                        dp[i+1][j+A[i]][Y] = min(dp[i+1][j+A[i]][Y], dp[i][j][k]+1)
                    # たこ焼きX個、たい焼きY個の上限どちらも超えない場合。
                    # dp[i+1][j+A[i]][k+B[i]]の値を埋める
                    else:
                        dp[i+1][j+A[i]][k+B[i]] = min(dp[i+1][j+A[i]][k+B[i]], dp[i][j][k]+1)

    if dp[-1][-1][-1] == N+1:
        print(-1)
    else:
        print(dp[-1][-1][-1])

if __name__ == '__main__':
    main()