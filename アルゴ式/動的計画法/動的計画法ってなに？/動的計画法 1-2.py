def main():
    N = int(input())
    A = list(map(int, input().split()))
    masu = [0]*N
    masu[1] = A[1]
    for i in range(2,N):
        masu[i] = min(masu[i-1]+A[i], masu[i-2]+2*A[i])
    print(masu[N-1])
if __name__ == '__main__':
    main()