def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    AA = [list(map(int, input().split())) for i in range(N)]
    M = int(input())
    NG_list = [[0]*N for i in range(N)]
    for i in range(M):
        X, Y = map(int, input().split())
        NG_list[X-1][Y-1] = 1
        NG_list[Y-1][X-1] = 1

    ans = 10**5 + 5

    # N人の選手と区画の組み合わせを順列全探索
    from itertools import permutations
    kumiawase = permutations(range(1, N+1))

    for kumi in kumiawase:
        tmp = 0
        bef_hito = 0
        now_hito = 0
        for kukaku, hito in enumerate(kumi):
            if kukaku == 0:
                bef_hito = hito
                now_hito = hito
                tmp += AA[hito-1][kukaku]
            else:
                bef_hito = now_hito
                now_hito = hito
                if NG_list[bef_hito-1][now_hito-1] == 1:
                    tmp = 10**5+5
                    break
                else:
                    tmp += AA[hito-1][kukaku]

        ans = min(ans, tmp)

    if ans > 10**5:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()