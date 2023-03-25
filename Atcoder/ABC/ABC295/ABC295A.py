def main():

    # 入力を受け取る
    N = int(input())
    A = list(input().split())
    eng = ['and', 'not', 'that', 'the', 'you']

    # 処理
    flg = False
    for w in A:
        if w in eng:
            flg = True
    
    # 答えを出力
    if flg:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()