def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S = list(input().rstrip())

    # 処理
    ans = 0

    # "atcoder"の先頭から一文字ずつswap回数を計算していく
    for chr in "atcoder":
        for i, s in enumerate(S):
            #　chrを正しい位置に移動するために必要なswap回数をansに加算
            if s == chr:
                ans += i
        # 計算完了した文字は文字列から除去
        S.remove(chr)
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()