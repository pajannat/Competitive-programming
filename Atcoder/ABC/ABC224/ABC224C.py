def main():
    from sys import stdin
    input = stdin.readline

    from itertools import combinations

    # 入力
    N = int(input())
    A = []
    for i in range(N):
        X, Y = map(int, input().split())
        A.append([X, Y])

    comb_list = list(combinations(range(N), 3))

    cnt = 0
    for i, j, k in comb_list:
        x1, y1 = A[i]
        x2, y2 = A[j]
        x3, y3 = A[k]
        x1 -= x3
        x2 -= x3
        y1 -= y3
        y2 -= y3
        if x1 * y2 == x2 * y1:
            continue

        cnt += 1

    # 答えを出力
    print(cnt)

if __name__ == '__main__':
    main()