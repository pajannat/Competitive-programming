def main():
    from sys import stdin
    input = stdin.readline

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    used_list = [0]*M

    cnt = 0
    for i in range(N):
        for j in range(M):
            if (A[i] <= B[j]) and used_list[j] == 0:
                cnt += 1
                used_list[j] = 1
                break

    print(cnt)

if __name__ == '__main__':
    main()