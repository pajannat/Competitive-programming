def main():
    from sys import stdin
    input = stdin.readline

    from collections import deque
    # 入力を受け取る
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 処理
    q = deque(A)
    for _ in range(K):
        q.popleft()
        q.append(0)
    
    # 答えを出力
    print(*q)


if __name__ == '__main__':
    main()