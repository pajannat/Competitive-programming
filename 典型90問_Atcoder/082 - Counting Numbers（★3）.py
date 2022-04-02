def main():
    from sys import stdin
    input = stdin.readline

    MOD = 10**9 + 7

    import math
    # 入力を受け取る
    L, R = map(int, input().split())

    ans = 0

    def keta_cnt(N):
        cnt = 1
        tmp = N
        while True:
            if tmp < 10:
                return cnt
            else:
                tmp //= 10
                cnt += 1

    # 処理
    ketaL = keta_cnt(L)
    ketaR = keta_cnt(R)

    for i in range(ketaL-1, ketaR):
        l = max(10**i, L)
        r = min(10**(i+1) - 1, R)
        Sn = ((r+l)*(r-l+1)//2)%MOD
        ans = (ans + Sn*(i+1))%MOD
    
    # 答えを出力
    print(ans)

if __name__ == '__main__':
    main()