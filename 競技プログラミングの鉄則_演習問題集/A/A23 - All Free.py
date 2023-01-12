def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]

    dp = [[10**9] * (2**N) for _ in range(M+1)]

    # 処理
    # bitDP
    # 初期化
    dp[0][0] = 0

    # 遷移処理
    # どのクーポンまで選べるか
    for i in range(M):
        # どの商品が無料か(無料である商品の集合を整数jで表現)
        for j in range(2**N):
            # 整数 j -> どの商品が無料であるかの 0, 1 二値のlist S に変換
            # 無料である商品の集合 S (クーポン適用前)
            S = [None] * N
            for k in range(N):
                # 整数 j をbit として見た場合, 下からk桁目のbitが立っているか？
                if (j // 2**k) % 2 == 0:
                    # 商品 k は無料でない
                    S[k] = 0
                else:
                    # 商品 k は既に無料である
                    S[k] = 1
            
            # クーポン i を適用した場合 の集合 S を計算
            for k in range(N):
                if A[i][k] == 1:
                    S[k] = 1
            
            # 集合S からクーポン i 適用後の集合の整数表現 v を計算
            v = 0
            for k in range(N):
                if S[k] == 1:
                    v += 2**k

            # 下に配る場合
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            # 右下に配る場合
            dp[i+1][v] = min(dp[i+1][v], dp[i][j] + 1)

    # 答えを出力
    # 出力
    if dp[M][2 ** N - 1] == 1000000000:
        print("-1")
    else:
        print(dp[M][2 ** N - 1])


if __name__ == '__main__':