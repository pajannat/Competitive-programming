def main():
    from sys import stdin
    input = stdin.readline

    class UnionFind: # uf = UnionFind(N)    N: 要素数
        # 初期化
        def __init__(self, n):
            self.par = [-1] * n
            self.rank = [0] * n
            self.siz = [-1] * n

        # 根を求める
        def root(self, x):
            # x が根の場合は x を返す
            if self.par[x] == -1:
                return x
            # 経路圧縮
            else:
                self.par[x] = self.root(self.par[x])
                return self.par[x]
        
        # x と y が同じグループに属するか (根が一致するか)
        def issame(self, x, y):
            return self.root(x) == self.root(y)

        # x を含むグループと y を含むグループを併合する
        def unite(self, x, y):
            # x 側と y 側の根を取得する
            rx = self.root(x)
            ry = self.root(y)
            # すでに同じグループのときは何もしない
            if rx == ry:
                return False
            # union by size
            # ry 側の rank が小さくなるようにする
            if self.rank[rx] > self.rank[ry]:
                rx, ry = ry, rx
            # ry を rx の子とする
            self.par[ry] = rx
            # rx 側の rank を調整する
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
            # rx 側の siz を調整する
            self.siz[rx] += self.siz[ry]
            return True
        
        # x を含む根付き木のサイズを求める
        def size(self, x):
            return siz[root(x)]

    # 入力
    N, M = map(int, input().split())
    AB = [map(int, input().split()) for i in range(M)]

    uf = UnionFind(N)
    for a, b in AB:
        uf.unite(a, b)

    # group_minidx[i] は
    # 頂点iを根とするグループの中で、最も番号が小さい頂点の番号
    group_minidx = [-1] * N
    # 番号の小さい方から順に格納し、既に格納済みの場合はスキップ
    for i in range(N):
        if group_minidx[uf.root(i)] == -1:
            group_minidx[uf.root(i)] = i

    # 出力
    for i in range(N):
        print(group_minidx[uf.root(i)])


if __name__ == '__main__':
    main()