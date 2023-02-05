"""
その日に工事する辺をランダムに選択
工事する辺の数は毎日最大 -> 工事をまとめて行い、後半を工事なしとする作戦

"""

def main():
    from sys import stdin
    input = stdin.readline

    import random

    # 入力を受け取る
    N, M, D, K = map(int, input().split())
    r = [0] * M
    weights = []
    for i in range(M):
        u, v, w = map(int, input().split())
        weights.append([i, u, v, w])

    weights.sort(key=lambda x: x[3], reverse=True)

    # 処理
    for i in range(1, D+1):
        if len(weights) == 0:
            break

        for _ in range(K):
            w = weights.pop()
            r[w[0]] = i
            if len(weights) == 0:
                break
    
    # 答えを出力
    print(*r)


if __name__ == '__main__':
    main()
