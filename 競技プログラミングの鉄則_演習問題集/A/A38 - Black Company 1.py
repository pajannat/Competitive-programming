def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    D, N = map(int, input().split())
    Day = [24] * (D+1)
    LRH = []
    for i in range(N):
        inp = list(map(int, input().split()))
        LRH.append(inp)
    
    # 処理
    for i in range(N):
        L, R, H = LRH[i]
        for j in range(L, R+1):
            Day[j] = min(Day[j], H)
    
    # 答えを出力
    print(sum(Day[1:]))


if __name__ == '__main__':
    main()