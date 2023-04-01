def main():

    # 入力を受け取る
    N = int(input())
    S = input().rstrip()

    # 処理
    flg = True
    bef_S = S[0]
    for i in range(1, N):
        now_S = S[i]
        if now_S == bef_S:
            flg = False
        bef_S = now_S

    
    # 答えを出力
    if flg:
        print("Yes")
    else:
        print("No")

 
if __name__ == "__main__":
    main()