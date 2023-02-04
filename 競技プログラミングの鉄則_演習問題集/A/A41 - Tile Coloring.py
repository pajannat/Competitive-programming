def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())
    S = input().rstrip()

    # 処理
    cnt = 1
    for i in range(1, N):
        if S[i] == S[i-1]:
            cnt += 1
        else:
            cnt = 1

        if cnt == 3:
            break

    
    # 答えを出力
    if cnt == 3:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()