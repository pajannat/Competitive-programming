def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    for k in range(1, N):
        pos = k
        while (pos != 0 ) and (A[pos-1] > A[pos]):
            A[pos-1], A[pos] = A[pos], A[pos-1]
            pos -= 1
        print(*A)

if __name__ == '__main__':
    main()