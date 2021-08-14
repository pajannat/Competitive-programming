def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    A_list = list(map(int,input().split()))
    sum = 0
    for A in A_list:
        if A <= 10:
            continue
        else:
            sum += (A-10)
            
    print(sum)

if __name__ == '__main__':
    main()