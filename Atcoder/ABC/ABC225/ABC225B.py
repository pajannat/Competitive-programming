def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N = int(input())
    G = [[] for i in range(N)]
    for i in range(N-1):
        A, B = map(int, input().split())
        A -= 1
        B -= 1

        # 頂点 A から頂点 B への辺を張る
        G[A].append(B)

        # 無向グラフの場合は次も実施
        G[B].append(A)
    
    cnt = [0] * N

    for g in G:
        for i in g:
            cnt[i] += 1

    max_cnt = max(cnt)

    # 出力
    if max_cnt == N-1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()