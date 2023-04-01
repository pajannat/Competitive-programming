def main():

    # 入力を受け取る
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    num_exist = set(A)
    flg = False

    # 処理
    for a in A:
        if (a + X) in num_exist:
            flg = True
    
    # 答えを出力
    if flg:
        print("Yes")
    else:
        print("No")

 
if __name__ == "__main__":
    main()