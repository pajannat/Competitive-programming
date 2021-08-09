def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())

    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))

    list_A = [0]*(N+1)
    for a in A:
        list_A[a] += 1

    list_B = [0]*(N+1)
    for c in C:
        list_B[B[c-1]] += 1

    sum = 0
    for i in range(N+1):
        sum += list_A[i]*list_B[i]

    print(sum)

if __name__ == '__main__':
    main()