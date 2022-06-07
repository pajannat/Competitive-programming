def main():
    from sys import stdin
    input = stdin.readline

    from collections import deque
    # 入力を受け取る
    N = int(input())
    # 配列を用意
    A = deque(list(range(1, N+1)))

    for i in range(2*N):
        # 要素の数が1つになったら終了
        if len(A) <= 1:
            break

        # 偶数回目は先頭の要素を削除
        if i % 2 == 0:
            A.popleft()
        # 奇数回目は先頭の要素を末尾へ移動
        else:
            A.append(A.popleft())

    # 答えを出力
    print(A[0])


if __name__ == '__main__':
    main()