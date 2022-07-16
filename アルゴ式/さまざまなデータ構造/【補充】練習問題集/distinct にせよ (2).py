def main():
    from sys import stdin
    input = stdin.readline

    from collections import defaultdict
    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    counter = defaultdict(lambda: 0)

    # 各整数の個数をカウント
    for a in A:
        counter[a] += 1
    
    # 削除するべき整数の個数の最小値を数える
    ans = 0
    for key in counter:
        # key == counter[key] の場合
        if key == counter[key]:
            diff = 0

        # key < counter[key] の場合
        elif key < counter[key]:
            diff = counter[key] - key

        # key > counter[key] の場合
        elif key > counter[key]:
            diff = counter[key]

        ans += diff

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()