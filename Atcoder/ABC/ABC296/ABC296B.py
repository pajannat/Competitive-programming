def main():

    # 入力を受け取る
    SS = []
    for _ in range(8):
        S = list(input().rstrip())
        SS.append(S)
    A = ["a", "b", "c", "d", "e", "f", "g", "h"]
    B = [str(i) for i in range(1, 9, 1)]
    ans = ""

    # 処理
    for i in range(8):
        for j in range(8):
            if SS[i][j] == "*":
                ans = A[j] + B[7 - i]
    
    # 答えを出力
    print(ans)

 
if __name__ == "__main__":
    main()