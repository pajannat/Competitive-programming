def main():
    from sys import stdin
    input = stdin.readline

    from itertools import combinations

    # 入力を受け取る
    N, W = map(int, input().split())
    A = list(map(int, input().split()))

    # 処理
    cntset = set()

    # 1つ選ぶ
    A1 = combinations(A, 1)
    for a1 in A1:
        if sum(a1) <= W:
            cntset.add(sum(a1))

    # 2つ選ぶ
    A2 = combinations(A, 2)
    for a2 in A2:
        if sum(a2) <= W:
            cntset.add(sum(a2))

    # 3つ選ぶ
    A3 = combinations(A, 3)
    for a3 in A3:
        if sum(a3) <= W:
            cntset.add(sum(a3))
    
    # 答えを出力
    print(len(cntset))


if __name__ == '__main__':
    main()