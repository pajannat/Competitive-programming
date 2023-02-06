def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N, K = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    ans = 0

    # 処理
    # 体力 A, 気力 B の下限値の組 (a, b) を全探索
    # a <= Ai <= a + K かつ, b <= Bi <= b + K となる生徒 i をカウント
    for a in range(1, 101):
        for b in range(1, 101):
            cnt = 0
            for i in range(N):
                if (a <= A[i] <= a + K) and (b <= B[i] <= b + K):
                    cnt += 1
            
            ans = max(ans, cnt)

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()