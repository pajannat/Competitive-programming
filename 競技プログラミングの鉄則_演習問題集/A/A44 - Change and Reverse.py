def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N, Q = map(int, input().split())
    A = list(range(1, N+1))
    Query = []
    for _ in range(Q):
        Query.append(list(map(int, input().split())))
    
    # 反転状態を管理するflg
    rev_flg = False

    # 処理
    for q in Query:
        if q[0] == 1:
            if rev_flg:
                A[N-q[1]] = q[2] 
            else:
                A[q[1]-1] = q[2]
        elif q[0] == 2:
            # 配列の反転
            rev_flg = not rev_flg
        elif q[0] == 3:
            if rev_flg:
                print(A[N-q[1]])
            else:
                print(A[q[1]-1])

    # 答えを出力


if __name__ == '__main__':
    main()