def main():
    from sys import stdin
    input = stdin.readline

    # ε₯ε
    N, M = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    ans = list(A - B)
    ans.sort()
    
    # εΊε
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()