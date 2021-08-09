def main():
    from sys import stdin
    input = stdin.readline
    N, A, B = map(int,input().split())

    sum = 0
    for num in range(1,N+1):
        num_sum = 0
        num_tmp = num
        for _ in range(len(str(num))):
            num_sum += num_tmp % 10
            num_tmp = num_tmp//10
        if num_sum>=A and num_sum<=B:
            sum += num

    print(sum)


if __name__ == '__main__':
    main()