def main():
    from sys import stdin
    input = stdin.readline

    N, M = map(int, input().split())
    S = list(input().split())
    T = list(input().split())

    kyuko = {}
    for t in T:
        kyuko[t] = 1

    for s in S:
        if s in kyuko:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()