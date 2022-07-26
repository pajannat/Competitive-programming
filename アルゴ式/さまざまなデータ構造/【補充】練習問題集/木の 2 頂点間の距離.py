def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())

    # 頂点iのparent
    P = [-1 for _ in range(N)]
    # 頂点iのchild
    children = [[] for i in range(N)]

    # children に値を格納
    for i in range(N-1):
        a, b = map(int, input().split())

        # child b の親はa
        P[b] = a

    u, v = map(int, input().split())

    # 頂点 u を始点とした、祖先との距離
    ances_u = [-1 for _ in range(N)] 
    # u -> u の距離は0
    ances_u[u] = 0
    # 現在みている頂点 now
    now = u

    # now が根でない限り、親方向に上り続ける
    while now != 0:
        # 今見ている頂点now の親par_now
        par_now = P[now]
        # uからpar_nowまでの距離
        ances_u[par_now] = ances_u[now] + 1
        # みる頂点をnowの親へと更新
        now = par_now


    # 頂点 v を始点とした、祖先との距離
    ances_v = [-1 for _ in range(N)] 
    # u -> u の距離は0
    ances_v[v] = 0
    # 現在みている頂点 now
    now = v

    # now が uの祖先でない限り、親方向に上り続ける
    # u, vの折り返し点でループを抜けることとなる
    while ances_u[now] == -1:
        # 今見ている頂点now の親par_now
        par_now = P[now]
        # vからpar_nowまでの距離
        ances_v[par_now] = ances_v[now] + 1
        # みる頂点をnowの親へと更新
        now = par_now
    
    # ans = u, v からの折り返し点までの距離
    ans = ances_u[now] + ances_v[now]

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()