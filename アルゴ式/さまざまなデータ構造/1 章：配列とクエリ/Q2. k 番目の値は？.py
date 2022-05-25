def main():
    from sys import stdin
    input = stdin.readline

    A = [3,1,4,1,5,9,2,6,5,3]
    # 入力を受け取る
    k = int(input())

    # 答えを出力
    print(A[k])


if __name__ == '__main__':
    main()