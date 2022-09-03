def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S = input().rstrip()
    youbi = {"Monday":1, "Tuesday":2, "Wednesday":3, "Thursday":4, "Friday":5}
    
    # 答えを出力
    print(6-youbi[S])


if __name__ == '__main__':
    main()