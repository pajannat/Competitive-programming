def main():
    from sys import stdin
    input = stdin.readline

    from collections import defaultdict
    # 入力を受け取る
    N = int(input())
    lose_cnt = defaultdict(lambda: 0)


    # 処理
    # 負けた数をカウント
    # 優勝者は負けた数0
    for _ in range(N-1):
        S1, score1, bar, score2, S2 = input().split()

        # S2の負け
        if int(score1) > int(score2):
            lose_cnt[S2] += 1
            # S1が未登録であれば新たに登録
            lose_cnt[S1]

        # S1の負け
        elif int(score1) < int(score2):
            lose_cnt[S1] += 1
            # S2が未登録であれば新たに登録
            lose_cnt[S2]
    

    # 答えを出力
    # 負けた数 0 の人が優勝者
    for key in lose_cnt.keys():
        if lose_cnt[key] == 0:
            print(key)


if __name__ == '__main__':
    main()