def main():
    from sys import stdin
    input = stdin.readline

    
    # 入力を受け取る
    S = list(input().rstrip())
    T = list(input().rstrip())
    ans = -1

    # 処理
    for i in range(len(S)):
        if S[i] == T[i]:
            pass
        else:
            ans = 1 + i
            print(ans)
            exit()
    
    # 末尾に1文字挿入された場合
    print(len(S)+1)


if __name__ == '__main__':
    main()