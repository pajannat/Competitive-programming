from collections import defaultdict

class UnionFind():
    """
    Union Find木クラス

    Attributes
    --------------------
    n : int
        要素数
    root : list
        木の要素数
        0未満であればそのノードが根であり、添字の値が要素数
    rank : list
        木の深さ
    """

    def __init__(self, n):
        """
        Parameters
        ---------------------
        n : int
            要素数
        """
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self, x):
        """
        ノードxの根を見つける

        Parameters
        ---------------------
        x : int
            見つけるノード

        Returns
        ---------------------
        root : int
            根のノード
        """
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        """
        木の併合

        Parameters
        ---------------------
        x : int
            併合したノード
        y : int
            併合したノード
        """
        x = self.find(x)
        y = self.find(y)

        if(x == y):
            return
        elif(self.rank[x] > self.rank[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def same(self, x, y):
        """
        同じグループに属するか判定

        Parameters
        ---------------------
        x : int
            判定したノード
        y : int
            判定したノード

        Returns
        ---------------------
        ans : bool
            同じグループに属しているか
        """
        return self.find(x) == self.find(y)

    def size(self, x):
        """
        木のサイズを計算

        Parameters
        ---------------------
        x : int
            計算したい木のノード

        Returns
        ---------------------
        size : int
            木のサイズ
        """
        return -self.root[self.find(x)]

    def roots(self):
        """
        根のノードを取得

        Returns
        ---------------------
        roots : list
            根のノード
        """
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_size(self):
        """
        グループ数を取得

        Returns
        ---------------------
        size : int
            グループ数
        """
        return len(self.roots())

    def group_members(self):
        """
        全てのグループごとのノードを取得

        Returns
        ---------------------
        group_members : defaultdict
            根をキーとしたノードのリスト
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    H, W = map(int, input().split())
    Q = int(input())

    uf = UnionFind(H*W)

    HW = [['.']*W for i in range(H)]
    dxdy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # 処理
    for i in range(Q):
        tmp_list = list(map(int, input().split()))
        if len(tmp_list) == 3:
            t, r, c = tmp_list
            idx = (r-1)*W + c
            R = r-1
            C = c-1
            HW[R][C] = "#"
            for dx, dy in dxdy:
                tmp_idx = (r-1+dy)*W + c+dx
                if 0 <= R+dy <= H-1 and 0 <= C+dx <= W-1:
                    if HW[R][C] == "#" and HW[R+dy][C+dx] == "#":
                        uf.unite(idx, tmp_idx)
        else:
            t, ra, ca, rb, cb = tmp_list
            idx_a = (ra-1)*W + ca
            idx_b = (rb-1)*W + cb
            if uf.same(idx_a, idx_b):
                if idx_a == idx_b and HW[ra-1][ca-1] == ".":
                    print("No")
                else:
                    print("Yes")
            else:
                print("No")


if __name__ == '__main__':
    main()