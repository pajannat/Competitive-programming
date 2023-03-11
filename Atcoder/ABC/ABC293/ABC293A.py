def main():

    # 入力を受け取る
    S = input().rstrip()
    ans = ""

    # 処理
    for i in range(1, len(S), 2):
        ans += S[i]
        ans += S[i-1]
    
    # 答えを出力
    print(ans)


if __name__ == "__main__":
    main()