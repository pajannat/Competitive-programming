def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    list_A = list(map(int,input().split()))
    sum_max = 0
    for l in range(N):
        min_A = 100000
        for r in range(l,N):
            tmp_sum = 0
            min_A = min(min_A,list_A[r])
            tmp_sum = (r-l+1)*min_A
            sum_max = max(sum_max,tmp_sum)
    print(sum_max)

if __name__ == '__main__':
    main()