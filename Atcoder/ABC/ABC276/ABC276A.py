def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S = list(input().rstrip())
    ans = -1

    # 処理
    for i in range(len(S)):
        if S[i] == 'a':
            ans = i + 1
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()