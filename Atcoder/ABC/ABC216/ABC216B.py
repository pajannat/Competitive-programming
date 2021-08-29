def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    names = []

    for _ in range(N):
        S, T = input().split()
        names.append((S, T))

    flg = False
    for i in range(N):
        S1, T1 = names[i]
        for j in range(i+1, N):
            S2, T2 = names[j]
            if (S1 == S2) and (T1 == T2):
                flg = True

    if flg:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()