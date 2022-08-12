def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, M = map(int, input().split())

    # 処理
    # 1~MのうちからN個とる組み合わせ
    from itertools import combinations
    ans = combinations(range(1, M+1), N)
    
    # 答えを出力
    for a in ans:
        print(*a)


if __name__ == '__main__':
    main()