def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    heap = list(map(int, input().split()))

    # 処理
    flg = True
    for i in range(1, N):
        parent_i = (i-1) // 2
        # 頂点iの親 >= 頂点i でなければFalse
        if heap[parent_i] < heap[i]:
            flg = False
        
    # 答えを出力
    if flg:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()