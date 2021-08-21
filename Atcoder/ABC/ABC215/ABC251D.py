def main():
    from sys import stdin
    input = stdin.readline

    import math

    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # (1~M)のうちフラグ0の数値が答え。フラグ1は答えから除外。
    chk = [0]*(M+1)

    # 素因数分解
    S = set()
    for i in range(N):
        for j in range(2, int(math.sqrt(A[i]))+1):
            while A[i] % j == 0:
                S.add(j)
                A[i] = A[i] // j
        if A[i] != 1:
            S.add(A[i])

    # 素因数sを持つkは除外するためにフラグ1をchk[k]に立てる
    # ↓TLE
    # for k in range(1, M+1):
    #     for s in S:
    #         if k % s == 0:
    #             chk[k] = 1
    # ↓計算量改善
    # (素因数sの倍数s_multは除外するためにフラグ1をchk[s_mult]に立てる)
    for s in S:
        if s <= M:
            chk[s] = 1
        s_mult = s + s
        while s_mult <= M:
            chk[s_mult] = 1
            s_mult += s
    
    # (1~M)のうち、chkのフラグが0の数値をansに格納
    ans = []
    for i in range(1, M+1):
        if chk[i] == 0:
            ans.append(i)

    ans.sort()
    print(len(ans))
    for s in ans:
        print(s)

if __name__ == '__main__':
    main()