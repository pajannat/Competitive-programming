def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    K = int(input())
    H = 21
    m = 0

    # 処理
    m += K

    H += m//60
    m = m - 60*(m//60)
    H = H % 24

    if len(str(m)) < 2:
        ans = str(H) + ":" + "0" + str(m)
    elif len(str(m)) == 2:
        ans = str(H) + ":" + str(m)
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()