def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S = list(input().rstrip())
    len_S = len(S)
    # dp[k][i] -> 最初左からi番目にいる子供が, 2**k 回移動後にいるマス
    dp = [[0] * len_S for _ in range(18)]

    # 処理
    # dp[0][i] -> 最初左からi番目にいる子供が, 2**0 回移動後にいるマス
    for i in range(len_S):
        # 左からi番目のマスの移動先は右
        if S[i] == "R":
            dp[0][i] = i + 1
        # 左からi番目のマスの移動先は左
        else:
            dp[0][i] = i - 1
    
    # dp[k][i] を求める. 
    # 繰り返し二乗法の要領で, 2**k 回移動後のマスを効率的に求める.
    # (2**(k-1) 移動後の結果を用いて, 2**k 回移動後のマスを求める)
    for k in range(1, 18):
        for i in range(len_S):
            # dp[k-1][dp[k-1][i]]
            #  -> 左からiマス目が2**(k-1)移動後のマス(dp[k-1][i])から,
            #     さらに2**(k-1)回移動後のマス(dp[k-1][dp[k-1][i]])
            dp[k][i] = dp[k-1][dp[k-1][i]]

    # 十分な回数移動後は特定の場所に落ち着く
    # 奇数回移動後の場合と, 偶数回移動後の場合でループする
    # 答えとなる10**100 回移動は偶数回移動
    # 偶数回の十分な回数(2**17)移動済みな dp[17] の結果を用いる
    ans = [0] * len_S
    for i in dp[17]:
        ans[i] += 1
    
    print(*ans)


if __name__ == '__main__':
    main()