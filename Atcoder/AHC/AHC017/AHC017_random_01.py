"""
その日に工事する辺をランダム選択
選択する数は毎日同じ数になるようにならす

"""

def main():
    from sys import stdin
    input = stdin.readline

    import random

    # 入力を受け取る
    N, M, D, K = map(int, input().split())
    r = [0] * M

    # 処理
    # 一日に工事する辺の数
    construct_num_per_day = min((M // D) + 1, K)
    edge = set(range(1, M+1))
    for i in range(1, D+1):
        sample_i = random.sample(edge, min(len(edge), construct_num_per_day))
        edge = edge - set(sample_i)
        for j in sample_i:
            r[j-1] = i
    
    # 答えを出力
    print(*r)


if __name__ == '__main__':
    main()