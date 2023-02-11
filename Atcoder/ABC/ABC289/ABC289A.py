def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    S = input().rstrip()
    ans = ""

    # 処理
    for s in S:
        if s == "0":
            ans += "1"
        else:
            ans += "0"
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()