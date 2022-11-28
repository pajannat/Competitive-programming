def main():
    from sys import stdin
    input = stdin.readline

    
    # Union-Find
    class UnionFind():
        # 初期化
        def __init__(self, n):
            self.par = [-1] * (n+1)
            for i in range(n):
                self.par[i] = i
            self.siz = [1] * n

        # 根を求める
        def root(self, x):
            if self.par[x] == x: return x # x が根の場合は x を返す
            else:
                self.par[x] = self.root(self.par[x]) # 経路圧縮
                return self.par[x]

        # x と y が同じグループに属するか (根が一致するか)
        def issame(self, x, y):
            return self.root(x) == self.root(y)

        # x を含むグループと y を含むグループを併合する
        def unite(self, x, y):
            # x 側と y 側の根を取得する
            rx = self.root(x)
            ry = self.root(y)
            if rx == ry: return False # すでに同じグループのときは何もしない
            # union by size
            if self.siz[rx] > self.siz[ry]: # ry 側の siz が小さくなるようにする
                rx, ry = ry, rx
            self.par[ry] = rx # ry を rx の子とする
            self.siz[rx] += self.siz[ry] # rx 側の siz を調整する
            return True
        
        # x を含む根付き木のサイズを求める
        def size(self, x):
            return self.siz[self.root(x)]

        

    # 入力を受け取る
    N, M = map(int, input().split())
    G = [[] for i in range(N+1)]

    for i in range(M):
        A, B = map(int, input().split())

        # 今回はunion-find で大きい順に頂点を配置していく
        # 配置した頂点より小さい頂点はその時点で存在しない
        # 小 -> 大 方向のみつなぐ

        # 頂点 A から頂点 B への辺を張る
        if A < B:
            G[A].append(B)

        # 無向グラフの場合は次も実施
        if B < A:
            G[B].append(A)

    ans = [0]
    cnt  = 0
    uf = UnionFind(N)

    # 処理
    for edge1 in range(N, 0, -1):
        # 頂点 edge1 を配置するので cnt += 1
        cnt += 1
        for edge2 in G[edge1]:
            if uf.issame(edge1, edge2):
                pass
            else:
                # edge1, edge2 をつなぐので cnt -= 1
                uf.unite(edge1, edge2)
                cnt -= 1
        # edge1からその時点で接続可能な頂点(edge1 > edge2 となるedge2)
        # をつなぎ終えたので ansに格納
        ans.append(cnt)
    
    # 答えを出力
    for i in range(N-1, -1, -1):
        print(ans[i])


if __name__ == '__main__':
    main()