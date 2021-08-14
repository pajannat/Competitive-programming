def main():
    from sys import stdin
    input = stdin.readline

    N, X = map(int, input().split())
    A = list(map(int,input().split()))
    A_gusu = []
    A_kisu = []
    for i in range(N):
        if i % 2 == 0:
            A_gusu.append(A[i])
        else:
            A_kisu.append(A[i] - 1)
    sum_A = sum(A_gusu) + sum(A_kisu)

    if X >= sum_A:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()