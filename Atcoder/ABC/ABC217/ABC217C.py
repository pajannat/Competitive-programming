def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    P = list(map(int, input().split()))
    Q = [0]*N

    P_dict = {}
    for i in range(N):
        P_dict[i] = P[i]

    for i in range(N):
        Q[P_dict[i]-1] = (i+1)

    print(*Q)

if __name__ == '__main__':
    main()