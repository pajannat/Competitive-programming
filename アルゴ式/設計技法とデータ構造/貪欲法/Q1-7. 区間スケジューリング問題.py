def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N = int(input())
    kukan = []
    for i in range(N):
        S, T = map(int, input().split())
        kukan.append([S, T])

    kukan.sort(key=lambda x:x[1])
    
    cnt = 0
    last_time = 0
    for k in kukan:
        S, T = k
        
        if S < last_time:
            continue

        cnt += 1
        last_time = T
      
    # 答えを出力
    print(cnt)

if __name__ == '__main__':
    main()