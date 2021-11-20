def main():
    from sys import stdin
    input = stdin.readline

    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    knew = [0] * (N+1)

    knew[X] = 1
    while True:
        X = A[X-1]
        if knew[X] == 1:
            break
        knew[X] = 1

    print(sum(knew))

if __name__ == '__main__':
    main()