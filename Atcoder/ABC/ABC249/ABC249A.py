def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    A, B, C, D, E, F, X = map(int, input().split())

    # 処理
    kyori_T = 0
    kyori_A = 0
    X_tmp = X
    for i in range(100):
        if A >= X_tmp:
            kyori_T += X_tmp*B
            break
        elif A < X_tmp <= A+C:
            kyori_T += A*B
            break
        # X_tmp > A+C の場合
        else:
            X_tmp -= (A+C)
            kyori_T += A*B

    X_tmp = X
    for i in range(100):
        if D >= X_tmp:
            kyori_A += X_tmp*E
            break
        elif D < X_tmp <= D+F:
            kyori_A += D*E
            break
        # X_tmp > D+F の場合
        else:
            X_tmp -= (D+F)
            kyori_A += D*E
    
    if kyori_T == kyori_A:
        print('Draw')
    elif kyori_T > kyori_A:
        print('Takahashi')
    else:
        print('Aoki')


if __name__ == '__main__':
    main()