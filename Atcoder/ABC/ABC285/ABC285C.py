def main():
    
    # 入力を受け取る
    S = input().rstrip()
    ans = 0

    # 処理
    AtoZ = {}
    for i, s in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        AtoZ[s] = i + 1
    for i, s in enumerate(S[::-1]):
        ans += 26 ** i * AtoZ[s]
    
    # 答えを出力
    print(ans)

 
if __name__ == "__main__":
    main()