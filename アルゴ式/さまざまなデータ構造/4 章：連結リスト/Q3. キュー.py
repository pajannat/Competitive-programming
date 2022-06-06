def main():
    from sys import stdin
    input = stdin.readline

    # 連結リストの各ノード
    class Node:
        def __init__(self, value=''):
            self.nex = None
            self.pre = None
            self.value = value
    
    # 連結リストの初期化
    nil = Node()
    nil.nex = nil
    nil.pre = nil
    
    # 連結リストへ先頭への要素の挿入
    def pushhead(v):
        # vを先頭Nodeにつなぐ
        v.nex = nil.nex
        # 先頭Nodeをvにつなぐ
        nil.nex.pre = v
        # vをnilにつなぐ
        v.pre = nil
        # nilをvにつなぐ
        nil.nex = v

    # 連結リストへ末尾からの要素の取り出し
    def poptail(v):
        # 末尾ノードを取得する
        tail = nil.pre
        # 返り値を格納
        ret = tail.value
        # 双方向連結リストが空なら"Error"を返す
        if tail == nil:
            ret = "Error"
        else:
            # tailのひとつ前をnilにつなぐ
            tail.pre.nex = nil
            # nilをtailのひとつ前につなぐ
            nil.pre = tail.pre
            # メモリを解放する
            del tail
        return(ret)

    
    # クエリ処理
    Q = int(input())
    for _ in range(Q):
        query = list(input().split())

        flg = int(query[0])

        # PushHead query
        if flg == 0:
            S = query[1]
            v = Node(S)
            pushhead(v)

        # PopTail query
        if flg == 1:
            print(poptail(nil.pre))


if __name__ == '__main__':
    main()