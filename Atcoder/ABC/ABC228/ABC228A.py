def main():
    from sys import stdin
    input = stdin.readline

    S, T, X = map(int, input().split())

    if S < T:
        if S <= X < T:
            print("Yes")
        else:
            print("No")
    elif S > T:
        if T <= X < S:
            print("No")
        else:
            print("Yes")

if __name__ == '__main__':
    main()