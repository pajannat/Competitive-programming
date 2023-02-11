def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    X = int(input())

    dp = [0] * (X+1)

    # 処理
    for b in B:
        dp[b] = -1
    
    dp[0] = 1
    for i in range(len(dp)):
        # i段目に到達可の場合
        if dp[i] == 1:
            for a in A:
                if i+a > X:
                    continue
                # dp[i+a] が通行止めでない場合
                if dp[i+a] != -1:
                    dp[i+a] = 1
    
    # 答えを出力
    if dp[-1] == 1:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()