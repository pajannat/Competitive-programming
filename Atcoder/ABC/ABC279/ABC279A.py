def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    S = input().rstrip()
    ans = 0

    # 処理
    for s in S:
        if s == "v":
            ans += 1
        elif s == "w":
            ans += 2
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()