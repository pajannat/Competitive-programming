def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = input().rstrip()

    # Nの桁数を求める
    len_N = len(N)
    N = int(N)

    cnt = 0
    # N-1桁目までの各桁について、数をカウント
    for i in range(1, len_N):
        n = 9 * (10**(i-1))
        cnt += int(n*(n+1)//2) % 998244353
    
    # N桁目について、数をカウント
    n = N - (10**(len_N-1) -1)
    cnt += int(n*(n+1)//2) % 998244353

    print(cnt % 998244353)

if __name__ == '__main__':
    main()
