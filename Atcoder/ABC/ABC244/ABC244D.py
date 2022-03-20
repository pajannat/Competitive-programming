def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S = list(input().split())
    T = list(input().split())

    cnt = 0
    for i in range(3):
        if S[i] == T[i]:
            cnt += 1
    
    if cnt == 0:
        print('Yes')
    elif cnt == 1:
        print('No')
    elif cnt == 3:
        print('Yes')

if __name__ == '__main__':
    main()