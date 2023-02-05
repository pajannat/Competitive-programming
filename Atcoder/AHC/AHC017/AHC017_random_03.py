"""
その日に工事する辺をランダム選択
選択する数は毎日同じ数になるようにならす
ランダムに2点サンプリングを繰り返して、到達不可の回数をカウント
カウントの少ない工事サンプリングを採用する

"""

# Union-Find 木
class unionfind:
    # n 頂点の Union-Find 木を作成
    # （ここでは頂点番号が 1-indexed になるように実装しているが、0-indexed の場合は par, size のサイズは n でよい）
    def __init__(self, n):
        self.n = n
        self.par = [ -1 ] * (n + 1) # 最初は親が無い
        self.size = [ 1 ] * (n + 1) # 最初はグループの頂点数が 1

    # 頂点 x の根を返す関数
    def root(self, x):
        # 1 個先（親）がなくなる（つまり根に到達する）まで、1 個先（親）に進み続ける
        while self.par[x] != -1:
            x = self.par[x]
        return x

    # 要素 u, v を統合する関数
    def unite(self, u, v):
        rootu = self.root(u)
        rootv = self.root(v)
        if rootu != rootv:
            # u と v が異なるグループのときのみ処理を行う
            if self.size[rootu] < self.size[rootv]:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]
            else:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]

    #  要素 u と v が同一のグループかどうかを返す関数
    def same(self, u, v):
        return self.root(u) == self.root(v)


def main():
    from sys import stdin
    input = stdin.readline


    import random


    # 入力を受け取る
    N, M, D, K = map(int, input().split())
    r = [0] * M
    score_loop_num = 2 * 10**4
    sample_loop_num = 10**2

    weights = []
    for i in range(M):
        u, v, w = map(int, input().split())
        weights.append([i, u, v, w])


    # 処理
    # 一日に工事する辺の数
    construct_num_per_day = min((M // D) + 1, K)
    edge = set(range(1, M+1))
    edge_all = set(range(1, M+1))
    for i in range(1, D+1):
        cnt = score_loop_num + 10
        sample_i = []
        for j in range(sample_loop_num):
            sample_j = random.sample(edge, min(len(edge), construct_num_per_day))
            # 交通止め以外の辺の集合
            j_edge = edge_all - set(sample_j)
            # 交通止め以外の辺でunion-find木作成
            uf_j = unionfind(N)
            for idx in j_edge:
                w = weights[idx-1]
                u_idx = w[1]
                v_idx = w[2]
                uf_j.unite(u_idx, v_idx)
            # uf_j に対して疑似スコア計算
            cnt_tmp = 0
            for k in range(score_loop_num):
                p, q = random.sample(range(1, N+1), 2)
                # 到達不可の場合にcnt_tmp += 1
                if uf_j.same(p, q) == False:
                    cnt_tmp += 1
            
            # 到達不可回数がcnt より少なければ sample_j を採用
            if cnt_tmp < cnt:
                # print(cnt_tmp, cnt)
                cnt = cnt_tmp
                sample_i = sample_j
            
            # 到達不可が0回の工事計画の場合は採用してループ終了
            if cnt == 0:
                break
        # print()


        # スコアのよかった工事計画 j で Day i に工事実施
        edge = edge - set(sample_i)
        for kouji_idx in sample_i:
            r[kouji_idx-1] = i
    
    # 答えを出力
    print(*r)


if __name__ == '__main__':
    main()