def main():
    from sys import stdin
    input = stdin.readline
    
    N = int(input())
    list_A = list(map(int,input().split()))

    XOR = 2**30 +10
    if N == 1:
        XOR = list_A[0]
    else:
        for i in range(1,2**(N-1)):
            XOR_tmp = 0
            OR = 0
            for j in range(N-1):
                OR = OR | list_A[j]
                if (i >> j) & 1: 
                    XOR_tmp = XOR_tmp ^ OR
                    OR = 0
            OR = OR | list_A[N-1]
            XOR_tmp = XOR_tmp ^ OR

            XOR = min(XOR,XOR_tmp)

    print(XOR)

if __name__ == '__main__':
    main()