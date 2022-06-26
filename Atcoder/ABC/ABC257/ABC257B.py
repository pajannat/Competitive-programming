def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    # 左からi番目のコマの場所
    ans = [a for a in A]
    # マスの状況
    masu = [-1 for _ in range(N+1)]

    # マスにコマを初期配置する
    for i, a in enumerate(A):
        idx = i+1
        masu[a] = idx
    

    # 処理
    for l in L:
        idx_Li = l-1
        # 左から L_i 番目のコマが一番右のマスにあるならば何も行わない。
        if ans[idx_Li] == N:
            pass
        else:
            # 1つ右のマスにコマがあるならば、何も行わない。
            if masu[ans[idx_Li]+1] != -1:
                pass
            else:
                # 左から L_i 番目のコマがあるマスの 1つ右のマスにコマが無いならば、
                # 1つ右のマスに移動させる。
                masu[ans[idx_Li]] = -1
                masu[ans[idx_Li]+1] = l
                ans[idx_Li] += 1
    
    # 答えを出力
    print(*ans)


if __name__ == '__main__':
    main()