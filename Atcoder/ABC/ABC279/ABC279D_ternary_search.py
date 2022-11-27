def main():
    from sys import stdin
    input = stdin.readline

    import math

    # 入力を受け取る
    A, B = map(int, input().split())
    l = 0
    r = A  # int(A/((math.sqrt(1))))

    # 地面到達にかかる時間 f(n)
    def f(n):
        return B*n + A/(math.sqrt(n+1))

    # 処理
    # 三分探索
    # 今回はl, r の差が1以下となれば十分 (f(n)のnが整数値のみであるため)
    while abs(l-r) > 1:
        m1 = (2*l+r)/3
        m2 = (l+2*r)/3
        if f(m1) < f(m2):
            # [m2, r]の区間に最小値がない
            # r -> m2 とする(右側を狭める)
            r = m2
        # f(m1) >= f(m2)
        else:
            # [l, m1)の区間に最小値がない
            # l -> m1 とする(左側を狭める)
            l = m1
    
    t = int(l)
    
    # 答えを出力
    print(min(f(max(0, t-1)), f(max(0, t)), f(max(0, t+1))))


if __name__ == '__main__':
    main()