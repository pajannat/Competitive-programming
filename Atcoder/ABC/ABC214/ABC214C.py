def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    dist_T = [10**16]*N
    dist_T[0] = T[0]
    for i in range(1, N):
        dist_T[i] = min(dist_T[i-1]+S[i-1], T[i])
    
    dist_T[0] = min(dist_T[-1]+S[-1], T[0])

    for i in range(1, N):
        dist_T[i] = min(dist_T[i-1]+S[i-1], T[i])
    
    dist_T[0] = min(dist_T[-1]+S[-1], T[0])

    for ans in dist_T:
        print(ans)

if __name__ == '__main__':
    main()