def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    H = int(input())
    # 高さ H のときの頂点番号 v の最大値
    max_v = 2**(H + 1) - 2
    Q = int(input())
    # query処理
    for _ in range(Q):
        flg, v = map(int, input().split())

        # 頂点 v の親の頂点番号を答える
        if flg == 0:
            # 該当する頂点が存在しない場合は −1 を出力
            if v == 0:
                print(-1)
            else:
                print((v-1)//2)

        # 頂点 v の左子頂点の番号を答える
        elif flg == 1:
            v_left_child = 2*v + 1
            # 該当する頂点が存在しない場合は −1 を出力
            if v_left_child > max_v:
                print(-1)
            else:
                print(v_left_child)
        
        # 頂点 v の右子頂点の番号を答える
        elif flg == 2:
            v_right_child = 2*v + 2
            # 該当する頂点が存在しない場合は −1 を出力
            if v_right_child > max_v:
                print(-1)
            else:
                print(v_right_child)


if __name__ == '__main__':
    main()