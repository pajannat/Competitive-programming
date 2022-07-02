def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())
    masu = [3*input().rstrip() for _ in range(N)]
    masu_9 = []
    for i in range(3):
        for m in masu:
            masu_9.append(list(m))


    # 処理
    ans = 0
    str_ans = ""
    for i in range(N,2*N):
        for j in range(N,2*N):

            # 上
            str_ans = ""
            for k in range(N):
                str_ans += masu_9[i-k][j]
            ans = max(ans, int(str_ans))
            
            # 下
            str_ans = ""
            for k in range(N):
                str_ans += masu_9[i+k][j]
            ans = max(ans, int(str_ans))

            # 右
            str_ans = ""
            for k in range(N):
                str_ans += masu_9[i][j+k]
            ans = max(ans, int(str_ans))

            # 左
            str_ans = ""
            for k in range(N):
                str_ans += masu_9[i][j-k]
            ans = max(ans, int(str_ans))

            # 右上
            str_ans = ""
            for k in range(N):
                str_ans += masu_9[i-k][j+k]
            ans = max(ans, int(str_ans))

            # 右下
            str_ans = ""
            for k in range(N):
                str_ans += masu_9[i+k][j+k]
            ans = max(ans, int(str_ans))

            # 左上
            str_ans = ""
            for k in range(N):
                str_ans += masu_9[i-k][j-k]
            ans = max(ans, int(str_ans))

            # 左下
            str_ans = ""
            for k in range(N):
                str_ans += masu_9[i+k][j-k]
            ans = max(ans, int(str_ans))
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()