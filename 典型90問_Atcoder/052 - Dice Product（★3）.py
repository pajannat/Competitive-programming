def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())

    MOD = 10**9 + 7

    ans = 1
    for i in range(N):
        A = list(map(int, input().split()))
        ans = ans*sum(A)%MOD
    
    print(ans)

if __name__ == '__main__':
    main()