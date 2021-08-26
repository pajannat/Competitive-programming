def main():
    N, X, Y = map(int, input().split())
    A = []
    A.append(X)
    A.append(Y)
    for i in range(2, N):
        tmp_A = (A[i-2]+A[i-1])%100
        A.append(tmp_A)
    print(A[N-1])
if __name__ == '__main__':
    main()