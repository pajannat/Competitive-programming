def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    F = [0]*(N+1)

    # 約数の個数のリストを作成
    for i in range(1, N+1):
        for j in range(i, N+1, i):
            F[j] += 1

    ans = 0
    for i in range(N+1):
        ans += i*F[i]
    
    print(ans)

if __name__ == '__main__':
    main()