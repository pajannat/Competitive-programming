def main():
    from sys import stdin
    input = stdin.readline

    # 二頂点間の距離を求める関数
    def calc_ijdist(i, j):
        Xi = A[i][0]
        Yi = A[i][1]
        Xj = A[j][0]
        Yj = A[j][1]

        return ((Xi-Xj)**2 + (Yi-Yj)**2)**(1/2)

    # 入力
    N = int(input())
    A = []
    for i in range(N):
        X, Y = map(int, input().split())
        A.append([X, Y])

    visited = set()
    visited.add(0)

    # 前回の頂点
    prev = 0

    dist = 0

    for i in range(N-1):
        ijdist_list = []
        for j in range(N):
            if j not in visited:
                ijdist_list.append([calc_ijdist(prev, j), j])
        min_dis, nex = min(ijdist_list)

        # 新たに頂点 nex を訪れる
        visited.add(nex)
        dist += min_dis

        # 前回頂点を更新
        prev = nex
    
    # 最後に頂点 0 へ戻る
    dist += calc_ijdist(prev, 0)

    # 答えを出力
    print(dist)

if __name__ == '__main__':
    main()