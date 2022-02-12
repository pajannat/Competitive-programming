def main():
    from sys import stdin
    input = stdin.readline

    import bisect

    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    index = bisect.bisect_left(A, X, 0, N-1)
    
    if A[index] == X:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()