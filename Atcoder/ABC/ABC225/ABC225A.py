def main():
    from sys import stdin
    input = stdin.readline

    # ε₯ε
    S = list(input().rstrip())
    L = len(set(S))
    
    # εΊε
    if L == 3:
        print(6)
    elif L == 2:
        print(3)
    elif L == 1:
        print(1)

if __name__ == '__main__':
    main()