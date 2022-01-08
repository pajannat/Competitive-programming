def main():
    from sys import stdin
    input = stdin.readline

    import heapq

    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    Pk = P[:K]
    heapq.heapify(Pk)

    # 答えを出力
    print(Pk[0])

    for i in range(K, N):
        Pk_min = Pk[0]
        if Pk_min <= P[i]:
            heapq.heappop(Pk)
            heapq.heappush(Pk, P[i])
            print(Pk[0])
        else:
            print(Pk[0])

if __name__ == '__main__':
    main()