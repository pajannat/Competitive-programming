def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, M, X = map(int, input().split())
    A = list(map(int, input().split()))
    cost = [0] * (N+1)

    ans = 101

    # 処理
    for a in A:
        cost[a] = 1
    
    ans = min(ans, sum(cost[:X]))
    ans = min(ans, sum(cost[X:]))
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()