def main():
    from sys import stdin
    input = stdin.readline

    # ε₯ε
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()

    # εΊε
    if N%2 == 0:
        print((A[(N//2)-1] + A[N//2])/2)
    else:
        print(A[(N-1)//2])


if __name__ == '__main__':
    main()