def main():
    from sys import stdin
    input = stdin.readline

    # ε₯ε
    N = int(input())
    lists = set()
    for i in range(N):
        lists.add('.'.join(input().split()))

    # εΊε
    print(len(lists))

if __name__ == '__main__':
    main()