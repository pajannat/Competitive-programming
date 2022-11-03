def main():
    from sys import stdin
    input = stdin.readline

    import math

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))

    # 処理
    # すべての A_i mod M が等しくなる Mがあるか探索
    # A_iを M で割ったあまりと、A_i+1を M で割ったあまりが一致する
    # <-> A_i - A_i+1 が M で割り切れる M
    # A1-A2, A2-A3, ..., A_N-1 - A_N をすべて割り切れる M 
    g = 0
    for i in range(N - 1):
        g = math.gcd(g, abs(A[i] - A[i + 1]))
    
    # 答えを出力
    # すべての A_i mod M が等しくなる Mがある場合
    if g == 1:
        print(2)
    # すべての A_i mod M が等しくなる Mがない場合
    else:
        print(1)


if __name__ == '__main__':
    main()