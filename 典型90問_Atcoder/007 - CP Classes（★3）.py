def main():
    from sys import stdin
    input = stdin.readline

    import bisect
    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    Q = int(input())

    # 生徒の最小不満度を算出、出力
    for i in range(Q):
        B = int(input())
        # 生徒の最適クラスを二分探索で探す
        j = bisect.bisect_left(A, B, lo=0, hi=N-1)
        diff = min(abs(A[j]-B), abs(A[j-1]-B))
        print(diff)
    
if __name__ == '__main__':
    main()