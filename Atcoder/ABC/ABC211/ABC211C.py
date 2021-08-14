def main():
    from sys import stdin
    input = stdin.readline

    S = input().rstrip()
    # 配列外参照を防ぐため、番兵として" "を追加
    S = " " + S
    T = " chokudai"

    # dpの入れ物を準備。0行目,0列目は番兵の値。
    dp = [[1]*(len(S)) if i == 0 else [0]*(len(S)) for i in range(9)]
    # 番兵の一つ内側の行,列からDPすることで配列外参照が起きない。
    for i in range(1, len(T)):
        for j in range(1, len(S)):
            if T[i] != S[j]:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = (dp[i][j-1] + dp[i-1][j-1]) % 1000000007
    
    print(dp[-1][-1] % 1000000007)

if __name__ == '__main__':
    main()