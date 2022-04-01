def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A_cnt = [0]*46
    B_cnt = [0]*46
    C_cnt = [0]*46

    ans = 0

    for i in range(N):
        A_cnt[A[i] % 46] += 1
        B_cnt[B[i] % 46] += 1
        C_cnt[C[i] % 46] += 1
    
    for i in range(46):
        for j in range(46):
            for k in range(46):
                if (i+j+k) % 46 == 0:
                    ans += A_cnt[i]*B_cnt[j]*C_cnt[k]

    print(ans)

if __name__ == '__main__':
    main()