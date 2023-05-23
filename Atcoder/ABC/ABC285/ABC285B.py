def main():
    
    # 入力を受け取る
    N = int(input())
    S = input().rstrip()

    # 処理
    for i in range(1, N):
        # l の初期化
        l = 0
        for j in range(N):
            # idx が範囲外の場合 または  S[j] == S[j+i] の場合は break
            if j+i >= N or S[j] == S[j+i]:
                break
            if S[j] != S[j+i]:
                l = (j+1)
        # 答えを出力
        print(l)

 
if __name__ == "__main__":
    main()