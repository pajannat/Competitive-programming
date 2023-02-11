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


    # 入力を受け取る
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    uf = unionfind(N+1)
    used = [0] * (N+1)
    ans = []

    # 処理
    for a in A:
        uf.unite(a, a+1)
    
    for i in range(1, N+1):
        tmp = []
        if used[i] == 0:
            tmp.append(i)
            used[i] = 1
        for j in range(i+1, N+1):
            # tmp = []
            if (used[j] == 0) and uf.same(i,j):
                tmp.append(j)
                used[j] = 1
        tmp.sort(reverse=True)
        ans.append(tmp)
    
    ans2 = []
    for an in ans:
        ans2 += an

    
    # 答えを出力
    # print(ans)
    print(*ans2)


if __name__ == '__main__':
    main()