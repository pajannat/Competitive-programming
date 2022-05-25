def main():
    from sys import stdin
    input = stdin.readline


    N, K = map(int, input().split())

    cnt = 0
    for i in range(N):
        cnt += min(N, K // (i+1))

    
    # 出力
    print(cnt)

if __name__ == '__main__':
    main()