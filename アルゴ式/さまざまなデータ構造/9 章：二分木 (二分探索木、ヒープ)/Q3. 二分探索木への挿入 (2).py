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
            node_v.par = now
            now.left = node_v
        # ・挿入したいキーが今いる頂点のキーより大きい場合
        elif v > now.value:
            node_v.par = now
            now.right = node_v
        
        return
    

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

    # 処理
    for i in range(Q):
        v = int(input())

        # 初回はrootの値として設定
        if i == 0:
            root.value = v
            continue
        
        # 値 v を入れたノード node_v を二分探索木に挿入する
        node_v = Node(v)
        insert(node_v)
    
    # 二分探索木の根から行きがけ順で探索してnumberに記録
    rec(root)

    # 二分探索木の探索順(行きがけ順)を出力
    print(*number)


if __name__ == '__main__':
    main()