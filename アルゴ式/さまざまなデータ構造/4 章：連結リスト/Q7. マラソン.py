def main():
    from sys import stdin
    input = stdin.readline

    from collections import deque
    # 入力を受け取る
    N = int(input())
    # 配列を用意
    A = list(map(int, input().split()))

    nex_list = [-1 for _ in range(N)]
    bak_list = [-1 for _ in range(N)]

    # 初期状態を反映
    for i in range(len(A)-1):
        p, q = A[i], A[i+1]
        nex_list[p] = q
        bak_list[q] = p


    # クエリ処理
    Q = int(input())
    for _ in range(Q):
        query = list(input().split())

        flg = int(query[0])

        # Overtake query
        if flg == 0:
            v = int(query[1])
            v_nex = nex_list[v]
            v_bak = bak_list[v]
            v_bak_bak = bak_list[v_bak]
            if v_bak == -1:
                print("Error")
            else:
                print(v_bak)

                # vとv_bakのnex_list, bak_listを更新
                if v_bak == -1:
                    pass
                else:
                    nex_list[v_bak] = v_nex
                    bak_list[v_bak] = v

                if v == -1:
                    pass
                else:
                    nex_list[v] = v_bak
                    bak_list[v] = v_bak_bak

                # v_bak_bakとv_nexのnex_list, bak_listを更新
                if v_bak_bak == -1:
                    pass
                else:
                    nex_list[v_bak_bak] = v

                if v_nex == -1:
                    pass
                else:
                    bak_list[v_nex] = v_bak


        # Dropout query
        if flg == 1:
            v = int(query[1])
            v_nex = nex_list[v]
            v_bak = bak_list[v]

            # v_nex, v_bakを連結
            if v_bak == -1:
                pass
            else:
                nex_list[v_bak] = v_nex
            
            if v_nex == -1:
                pass
            else:
                bak_list[v_nex] = v_bak
            # vの連結を解除
            nex_list[v] = -1
            bak_list[v] = -1


if __name__ == '__main__':
    main()