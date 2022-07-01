def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())
    # 頂点iのparent
    P = [-1] + list(map(int, input().split()))
    # クエリの数
    Q = int(input())

    # 頂点iのchild
    children = [[] for i in range(N)]
    # 箱内部にある箱の個数
    inner_box_cnt = [-1 for _ in range(N)]

    # children に値を格納
    for i in range(N):
        # i == 0 はスキップ
        if i == 0:
            continue

        A = i
        B = P[i]

        # parent Bの childに Aを追加
        children[B].append(A)


    # 箱内部の箱の個数をカウント
    def rec(v, children):
        # 既にinner_box_cnt[v]を計算済みの場合
        if inner_box_cnt[v] != -1:
            return inner_box_cnt[v]

        # inner_box_cnt[v]が未計算の場合

        # 箱vに直接入っている箱の数をカウント
        ans = len(children[v])

        # 箱番号の若い順に箱を開ける (関数の再帰)
        for v2 in children[v]:
            ans += rec(v2, children)
        
        # inner_box_cnt[v]にcntをメモ
        inner_box_cnt[v] = ans
        return ans
    
    # # 箱 0 を始点として inner_box_cnt に記録する
    # (箱 0 から始めることで全ての箱についての情報を計算)
    rec(0, children)

    
    # 答えを出力
    for _ in range(Q):
        # 入力を受け取る
        v = int(input())
        
        # 答えを出力
        print(inner_box_cnt[v])
    

if __name__ == '__main__':
    main()