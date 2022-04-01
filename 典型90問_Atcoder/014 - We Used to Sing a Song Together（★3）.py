def main():
    from sys import stdin
    input = stdin.readline

    import bisect
    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    B.sort()

    ans = 0

    for i in range(N):
        ans += abs(A[i]-B[i])
    
    print(ans)
    
if __name__ == '__main__':
    main()