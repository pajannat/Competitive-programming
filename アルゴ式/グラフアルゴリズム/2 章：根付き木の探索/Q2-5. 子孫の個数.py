def main():
    from sys import stdin
    input = stdin.readline

    from collections import deque
    import sys

    # スタックオーバーフローを防ぐ
    sys.setrecursionlimit(int(1E+5))

    # 入力
    N = int(input())
    A = list(map(int, input().split()))

    G = [[] for _ in range(N)]

    for i in range(N-1):
        # 頂点A[i]から頂点 i+1 への辺を張る
        G[A[i]].append(i+1)


    dp = [0] * N

    def f(v):
        for i in G[v]:
            dp[v] = dp[v] + (f(i) + 1)
            
        return dp[v]

    f(0)

    # 答えを出力
    for ans in dp:
        print(ans)


if __name__ == '__main__':
    main()