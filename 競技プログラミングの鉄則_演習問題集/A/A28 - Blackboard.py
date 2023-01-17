def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    T = []
    A = []
    for _ in range(N):
        t, a = input().split()
        T.append(t)
        A.append(int(a))
    
    ans = 0

    # 処理
    for i in range(N):
        if T[i] == "+":
            ans += A[i]
        elif T[i] == "-":
            ans -= A[i]
        elif T[i] == "*":
            ans *= A[i]
        
        ans %= 10000

        # 答えを出力
        print(ans)


if __name__ == '__main__':
    main()