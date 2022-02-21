def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, X, Y = map(int, input().split())

    flg1 = False
    flg2 = False

    if N >= abs(X)+abs(Y):
        flg1 = True
    
    if (N-abs(X)-abs(Y))%2 == 0:
        flg2 = True

    # 答えを出力
    if flg1 and flg2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()