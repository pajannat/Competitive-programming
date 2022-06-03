def main():
    from sys import stdin
    input = stdin.readline

    # 連結リストの各ノード
    class Node:
        def __init__(self, value=''):
            self.nex = None
            self.value = value
    
    # 連結リストの初期化
    nil = Node()
    nil.nex = nil
    
    # 連結リストへ先頭への要素の挿入
    def insert(v):
        # 先頭Nodeにvをつなぐ
        v.nex = nil.nex
        # nilをvにつなぐ
        nil.nex = v
    
    # クエリ処理
    Q = int(input())
    for _ in range(Q):
        query = list(input().split())

        flg = int(query[0])

        # Insert query
        if flg == 0:
            S = query[1]
            v = Node(S)
            insert(v)

        # Output query
        if flg == 1:
            output_list = []
            k = int(query[1])
            v = nil.nex
            for i in range(k):
                if v == nil:
                    break
                else:
                    output_list.append(v.value)
                v = v.nex
            print(*output_list)


if __name__ == '__main__':
    main()