def main():
    from sys import stdin
    input = stdin.readline

    from itertools import combinations
    # 入力を受け取る
    N, M = map(int, input().split())
    S_list = []
    for _ in range(M):
        C = int(input())
        A = list(map(int, input().split()))
        S_list.append(set(A))
    ans = 0

    # 処理
    # S_listからの取り出し方の全探索
    for k in range(1, M+1):
        for comb in combinations(S_list, k):
            tmp = set([])
            for c in comb:
                tmp = tmp | c
            if len(tmp) == N:
                ans += 1

    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()