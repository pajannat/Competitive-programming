def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N = int(input())
    A = list(map(int, input().split()))
    # B = [[番号, 点数, 順位]]
    B = [[i, A[i], 0] for i in range(N)]
    B.sort(key=lambda x: x[1], reverse=True)

    cnt = 0
    for i in range(1, N):
        if B[i-1][1] == B[i][1]:
            pass
        else:
            cnt += 1
        B[i][2] = cnt
    
    B.sort()
    # 出力
    for i in range(N):
        print(B[i][2])

if __name__ == '__main__':
    main()