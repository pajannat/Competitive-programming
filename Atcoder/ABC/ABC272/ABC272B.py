def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, M = map(int, input().split())
    check = [[0]*N for _ in range(N)]

    # 処理
    for i in range(M):
        A = list(map(int, input().split()))
        for j in range(1, len(A)):
            for k in range(1, len(A)):
                check[A[j]-1][A[k]-1] = 1
    
    # 答えを出力
    for chk in check:
        for num in chk:
            if num == 0:
                print("No")
                exit()
    
    print("Yes")


if __name__ == '__main__':
    main()