def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A, B, C = map(int, input().split())

    ans = 10**9

    for i in range(10000):
        for j in range(10000):
            tmp = N - A*i - B*j
            if tmp >= 0 and tmp % C == 0:
                ans = min(ans, i+j+(tmp//C))
    
    print(ans)

if __name__ == '__main__':
    main()