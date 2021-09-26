def main():
    from sys import stdin
    input = stdin.readline

    K = int(input())
    A, B = map(str, input().split())
    A_10 = 0
    B_10 = 0

    for i in range(len(A)):
        A_10 += (K**i)*int(A[len(A)-1-i])

    for i in range(len(B)):
        B_10 += (K**i)*int(B[len(B)-1-i])

    ans = A_10 * B_10

    print(ans)

if __name__ == '__main__':
    main()