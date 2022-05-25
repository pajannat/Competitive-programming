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
    N, Q = map(int, input().split())
    W = list(map(int, input().split()))
    txy = [list(map(int, input().split())) for i in range(Q)]

    uf = UnionFind(N)

    for t, x, y in txy:
        if t == 0:
            if not uf.issame(x, y):
                # x, y 併合前の、x, yの根を保持
                root_x = uf.root(x)
                root_y = uf.root(y)
                uf.unite(x, y)
                # x, y 併合後の、x, yの根をROOTとする
                ROOT = uf.root(x)

                # x, y 併合後の塊の重さを計算する
                if ROOT == root_x:
                    # root_yがroot_xの子となる場合
                    W[ROOT] += W[root_y]
                else:
                    # root_xがroot_yの子となる場合
                    W[ROOT] += W[root_x]
        elif t == 1:
            print(W[uf.root(x)])

if __name__ == '__main__':
    main()