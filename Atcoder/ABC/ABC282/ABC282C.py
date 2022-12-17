def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())
    S = input().rstrip()
    ans = ""
    cnt = 0

    # 処理
    for i in range(N):
        tmp = [S[i]]

        if tmp[0] == '"':
            cnt += 1

        if tmp[0] == ",":
            # ""で囲われているstate
            if cnt % 2 == 1:
                pass
            # ""で囲われていないstate
            else:
                tmp[0] = "."
        
        ans += tmp[0]
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()