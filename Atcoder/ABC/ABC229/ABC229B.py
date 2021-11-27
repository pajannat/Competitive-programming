def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    A, B = input().split()

    easy_flg = True
    calc_len = min(len(A), len(B))
    for i in range(1, calc_len+1):
        if int(A[-i])+int(B[-i]) >= 10:
            easy_flg = False

    # # 出力
    if easy_flg:
        print("Easy")
    else:
        print("Hard")

if __name__ == '__main__':
    main()