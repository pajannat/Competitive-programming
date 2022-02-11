def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    cnt_L = [0]*100001
    for a in A:
        cnt_L[a] += 1
    
    ans = 0
    for a in range(50001):
        if 100000-a == 50000:
            ans += cnt_L[a]*(cnt_L[a]-1)//2
        else:
            ans += cnt_L[a]*cnt_L[100000-a]

    print(ans)

if __name__ == '__main__':
    main()