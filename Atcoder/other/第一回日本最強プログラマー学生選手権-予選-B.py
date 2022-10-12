def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 処理
    # A内の転倒数を数える
    cnt_internal = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] > A[j]:
                cnt_internal += 1
    cnt_internal = (cnt_internal * K) % (10**9 + 7)

    # A間の転倒数を数える
    cnt_between = 0
    for a1 in A:
        for a2 in A:
            if a1 > a2:
                cnt_between += 1
    cnt_between = (cnt_between * K * (K - 1) // 2) % (10**9 + 7)
    
    ans = (cnt_internal + cnt_between) % (10**9 + 7)

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()