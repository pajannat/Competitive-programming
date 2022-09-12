def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S = input().rstrip()

    # 処理
    # 各白石の移動した距離の総和が操作回数
    # 各白石と相対順序が入れ替わった石の数は, 
    # それよりもはじめ左にあった黒石の数

    # tmp_cnt は番号 i 時点での黒石の数の総和
    tmp_cnt = 0
    # cnt は操作回数の総和
    # 白石が出てきた時点で, それより左にある黒石の数(tmp_cnt)を加算
    cnt = 0
    for s in S:
        if s == "B":
            tmp_cnt += 1
        elif s == "W":
            cnt += tmp_cnt
    
    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()