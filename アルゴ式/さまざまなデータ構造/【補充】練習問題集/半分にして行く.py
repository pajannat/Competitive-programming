def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N, K = map(int, input().split())
    # 最大値を管理するために -1倍する
    A = list(map(lambda x:-int(x), input().split()))

    import heapq
    heapq.heapify(A)

    # 処理
    for _ in range(K):
        # Aの最大値
        max_A = -heapq.heappop(A)

        # max_A を 2 で割った商
        quotient_max_A = max_A // 2

        # A に max_A を 2 で割った商 quotient を追加する
        heapq.heappush(A, -quotient_max_A)
    
    # K 回の操作を実施したあとの N 個の整数の総和を求める
    ans = -sum(A)
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()