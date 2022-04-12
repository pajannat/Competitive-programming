def main():
    from sys import stdin
    input = stdin.readline

    MOD = 10**9 + 7
    # 入力を受け取る
    K = int(input())

    # dp[i]は各桁の数字の和がiとなる数字Xの個数
    dp = [0]*(K+1)

    # 処理
    # dp[K]を求める。
    if K % 9 != 0:
        print(0)
    else:
        dp[0] = 1
        for i in range(1, K+1):
            if i <= 9:
                for j in range(1, i+1):
                    dp[i] = (dp[i] + dp[i-j]) % MOD
            else:
                # 数字Xの先頭が 1 <= j <= 9 の場合, Xの2桁目以降の和はi-jの倍数
                # ("先頭のj + 2桁目以降 = iの倍数"であるため)
                # -> dp[i]はdp[i-j](1 <= j <= 9)の合計
                for j in range(1, 10):
                    dp[i] = (dp[i] + dp[i-j]) % MOD
        print(dp[K])


if __name__ == '__main__':
    main()