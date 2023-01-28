def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    cnt_For = 0
    cnt_Against = 0

    # 処理
    for i in range(N):
        S = input().rstrip()
        if S == "For":
            cnt_For += 1
    
    cnt_Against = N - cnt_For
    
    # 答えを出力
    if cnt_For > cnt_Against:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()