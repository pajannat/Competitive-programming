def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    S = input().rstrip()
    from collections import defaultdict
    d = defaultdict(lambda: 0)

    # 処理
    for s in S:
      d[s] += 1

    # 答えを出力
    for key in d.keys():
      if d[key] == 1:
        print(key)
        exit()
    
    print(-1)


if __name__ == '__main__':
    main()