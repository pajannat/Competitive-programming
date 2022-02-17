def main():
    from sys import stdin
    input = stdin.readline

    N, M = map(int, input().split())
    adj = [[] for i in range(N+1)]
    for i in range(1, M+1):
        A, B = map(int, input().split())
        adj[A].append(B)
        # ↓無向グラフの場合は#をとる
        adj[B].append(A)
    
    ans = 0
    for i in range(1, N+1):
        cnt = 0
        for a in adj[i]:
            if i > a:
                cnt += 1
        
        if cnt == 1:
            ans += 1
    
    print(ans)


if __name__ == '__main__':
    main()