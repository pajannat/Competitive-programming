def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    a, b, c = map(int, input().split())

    # 処理
    abc_sort = [a, b, c]
    abc_sort.sort()
    
    # 答えを出力
    if abc_sort[1] == b:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()