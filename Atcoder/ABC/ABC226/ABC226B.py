def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N = int(input())
    lists = set()
    for i in range(N):
        lists.add('.'.join(input().split()))

    # 出力
    print(len(lists))

if __name__ == '__main__':
    main()