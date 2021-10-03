def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())

    # ninzu[k] = nはログイン人数がk人である期間がn日を表す。
    ninzu = [0]*(N+1)

    loginout = []

    for i in range(N):
        A, B = map(int, input().split())
        start = A
        end = A + B
        loginout.append((start, 1))
        loginout.append((end, -1))

    loginout.sort()
    cumsum = 0
    daycursor = 0

    for day, x in loginout:
        ninzu[cumsum] += day - daycursor
        daycursor = day
        cumsum += x

    print(*ninzu[1:])

if __name__ == '__main__':
    main()