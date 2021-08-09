def main():
    from sys import stdin
    input = stdin.readline

    N,M = map(int,input().split())

    conditions = []
    for idx in range(M):
        A,B = map(int,input().split())
        conditions.append([A,B])
    
    K = int(input())
    actions = []
    for j in range(K):
        C,D = map(int,input().split())
        actions.append([C,D])
    
    cnt_max = 0
    for i in range(2 ** K):
        cnt = 0
        s = set()
        for j in range(K):
            s.add(actions[j][(i >> j) & 1])
        for cnd in conditions:
            if cnd[0] in s and cnd[1] in s:
                cnt += 1
        cnt_max = max(cnt_max,cnt)

    print(cnt_max)

if __name__ == '__main__':
    main()