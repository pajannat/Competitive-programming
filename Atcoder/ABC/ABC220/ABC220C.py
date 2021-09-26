def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    cnt = 0

    sum_A = sum(A)
    a = X // sum_A
    S = a * sum_A
    cnt = N*a
    for i in range(N):
        if S > X:
            break
        else:
            S += A[i]
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()