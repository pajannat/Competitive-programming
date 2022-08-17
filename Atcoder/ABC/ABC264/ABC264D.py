def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S = list(input().rstrip())

    # 処理
    ans = 0

    for chr in "atcoder":
        for i, s in enumerate(S):
            if s == chr:
                ans += i
        S.remove(chr)
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()