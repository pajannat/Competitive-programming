def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    H, W = map(int, input().split())
    HW = [None] * (H*W + 1)

    ans = 0

    # 処理
    for i in range(1, H+1):
        P = [-1] + list(map(int, input().split()))
        for j in range(1, W+1):
            HW[(i-1)*W + j] = P[j]
    
    # 制約の小さいHでbit全探索
    # 2進数 H桁を考える
    for i in range(2 ** H):
        H_list = []
        W_list = []
        # 2進数 H桁のうち、bitが立っているところ(1)を採用
        for j in range(H):
            if (i >> j) & 1:
                H_list.append(j+1)
        
        cnt_P = [0] * (H*W + 1)
        if len(H_list) != 0:
            # W列について、H_list行すべてが同じ数字かチェック
            for k in range(1, W+1):
                # チェックフラグ
                flg = True
                # チェック処理
                tmp = HW[(H_list[0]-1)*W + k]
                for h in H_list:
                    if tmp == HW[(h-1)*W + k]:
                        pass
                    else:
                        flg = False
                # チェック後処理。カウントに加算
                if flg:
                    W_list.append(k)
                    # 数字Pについて、チェックが通った回数を記録
                    cnt_P[HW[(H_list[0]-1)*W + k]] += 1

        # 今回のH_listのパターンについて、カウント最高値であればansを更新
        # max(cnt_P) -> チェック通過した列が一番多い数字Pのカウント
        cnt = max(cnt_P) * len(H_list)
        if cnt > ans:
            ans = cnt

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()