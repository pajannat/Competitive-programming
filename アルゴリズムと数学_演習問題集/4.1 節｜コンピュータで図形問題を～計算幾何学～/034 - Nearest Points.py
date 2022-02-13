def main():
    from sys import stdin
    input = stdin.readline

    import math

    def dist_AB(A, B):
        ans = math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)
        return ans

    N = int(input())

    A = []
    for i in range(N):
        x, y = map(int, input().split())
        A.append([x, y])

    ans = 10**8
    for i in range(N):
        for j in range(N):
            if i != j:
                ans = min(ans, dist_AB(A[i], A[j]))

    print(ans)

if __name__ == '__main__':
    main()