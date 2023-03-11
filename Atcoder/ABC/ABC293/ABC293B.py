def main():

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    called = [0] * N
    ans = []

    # 処理
    for i in range(N):
        if called[i] == 0:
            called[A[i]-1] = 1

    
    # 答えを出力
    print(N - sum(called))
    for i in range(N):
        if called[i] == 0:
            ans.append(i+1)
    print(*ans)


if __name__ == "__main__":
    main()