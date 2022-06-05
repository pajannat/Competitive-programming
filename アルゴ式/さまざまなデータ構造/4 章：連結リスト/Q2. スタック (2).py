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

    # 連結リストへ先頭への要素の挿入
    def pophead(v):
        # 先頭ノードを取得する
        head = nil.nex
        # nilをv.nexにつなぐ
        nil.nex = v.nex
        # メモリを解放する
        del head
    
    # クエリ処理
    Q = int(input())
    for _ in range(Q):
        query = list(input().split())

        flg = int(query[0])

        # PushHead query
        if flg == 0:
            S = query[1]
            v = Node(S)
            insert(v)

        # PopHead query
        if flg == 1:
            head_node = nil.nex
            value = head_node.value
            if value == "":
                print("Error")
            else:
                print(value)
            pophead(head_node)


if __name__ == '__main__':
    main()