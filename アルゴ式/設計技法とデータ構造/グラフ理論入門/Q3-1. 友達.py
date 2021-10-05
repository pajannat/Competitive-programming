def main():
    from sys import stdin
    input = stdin.readline

    N, A, B = map(int, input().split())

    S = []
    for i in range(N):
        S.append(input().rstrip())
    
    if S[A][B] == "o":
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()