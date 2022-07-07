def main():
    from sys import stdin
    input = stdin.readline


    class Node:
        def __init__(self, value=0):
            # 親
            self.parent = None
            # 左の子頂点
            self.left = None
            # 右の子頂点
            self.right = None
            # ノードに付随している値
            self.value = value


    # 根のノードを宣言 (insert や rec 関数のためにグローバルに置いた)
    root = Node()


    # node_vを二分木に挿入する関数
    def insert(node_v):
        # 根頂点から順番に見ていき、
        v = node_v.value
        nex, now = root, Node()

        while nex:
            now = nex
            # ・挿入したいキーが今いる頂点のキー以下である場合は左側の子頂点へ進む
            if v <= now.value:
                nex = now.left
            # ・挿入したいキーが今いる頂点のキーより大きい場合は右側の子頂点へ進む
            elif v > now.value:
                nex = now.right

        # 進む先の子頂点が存在しなくなったとき
        # ・挿入したいキーが今いる頂点のキー以下である場合
        if v <= now.value:
            node_v.parent = now
            now.left = node_v
        # ・挿入したいキーが今いる頂点のキーより大きい場合
        elif v > now.value:
            node_v.parent = now
            now.right = node_v
        
        return

    # node_vが二分木に存在するか検索する関数
    def find(node_v):
        # 根頂点から順番に見ていき、
        v = node_v.value
        nex, now = root, Node()
        find_flg = False

        while nex:
            now = nex
            # ・node_v.value が今いる頂点のキーと一致する場合は、探索を打ち切る
            if v == now.value:
                find_flg = True
                return find_flg
            # ・node_v.value が今いる頂点のキー以下である場合は左側の子頂点へ進む
            elif v <= now.value:
                nex = now.left
            # ・node_v.value が今いる頂点のキーより大きい場合は右側の子頂点へ進む
            elif v > now.value:
                nex = now.right
        
        return find_flg


    # ノード node_v を根とする部分木のうち、キーが最小のノードを返す関数
    def min_node(node_v):
        # 左の子頂点が存在するならば、そちらに進む
        if node_v.left:
            return min_node(node_v.left)
        # そうでないならば、node_v を返す
        else:
            return node_v

    # key_vを持つnodeを二分木から削除する関数
    def delete(key_v):
        # node_v を検索
        # 根頂点から順番に見ていき、
        v = key_v
        now = root
        find_flg = False

        while now:
            # ・node_v.value が今いる頂点のキーと一致する場合は、探索を打ち切る
            if v == now.value:
                find_flg = True
                break
            # ・node_v.value が今いる頂点のキー以下である場合は左側の子頂点へ進む
            elif v <= now.value:
                now = now.left
            # ・node_v.value が今いる頂点のキーより大きい場合は右側の子頂点へ進む
            elif v > now.value:
                now = now.right

        # node_v が見つからなかった場合は打ち切り
        if find_flg == False:
            return find_flg

        # node_v の子頂点をカウント
        child_cnt = 0
        if now.left:
            child_cnt += 1
        if now.right:
            child_cnt += 1

        # node が子頂点を持たない場合
        if child_cnt == 0:
            # par の子頂点の情報を書き換えて、node を削除
            par = now.parent
            if par.left == now:
                par.left = None
            elif par.right == now:
                par.right = None
            
            del now

        # node がちょうど 1 つの子頂点 ch を持つ場合
        elif child_cnt == 1:
            # par と ch の情報を書き換えて、node を削除
            par = now.parent
            ch = None

            # chにnowの子を格納
            if now.left:
                ch = now.left
            elif now.right:
                ch = now.right

            # nowのparentにnowの子をつなぐ
            ch.parent = par
            if par.left == now:
                par.left = ch
            elif par.right == now:
                par.right = ch
            
            del now

        # node が 2 つの子頂点を持つ場合:
        elif child_cnt == 2:
            # 通りがけ順で node の次の頂点 nex を求めます
            nex_key = min_node(now.right).value
            # node のキーを、nex のキーに書き換えて、nex を削除
            delete(nex_key)
            now.value = nex_key

        return find_flg
    

    # 頂点番号を記録する配列
    number = []

    # ノード node から行きがけ順で二分木を探索してnumberに記録
    def rec(node):
        # node.value をnumberに記録
        number.append(node.value)

        # node.left が None でなければ rec(node.left)
        if node.left != None:
            rec(node.left)

        # node.right が None でなければ rec(node.right)
        if node.right != None:
            rec(node.right)
        
        return


    # 入力を受け取る
    Q = int(input())
    # query処理
    for _ in range(Q):
        query = list(input().split())

        flg = int(query[0])
        v = int(query[1])

        # insert query
        if flg == 0:
            # 値 v を入れたノード node_v を二分探索木に挿入する
            node_v = Node(v)
            insert(node_v)

        # find query
        elif flg == 1:
            # 値 v を入れたノード node_v が存在するか二分探索木を検索する
            node_v = Node(v)
            find_flg = find(node_v)
            if find_flg:
                print("Yes")
            else:
                print("No")
        
        # delete query
        elif flg == 2:
            # 値 v を持つノード node_v を二分探索木から削除
            delete_flg = delete(v)
            if delete_flg:
                print("Complete")
            else:
                print("Error")


if __name__ == '__main__':
    main()