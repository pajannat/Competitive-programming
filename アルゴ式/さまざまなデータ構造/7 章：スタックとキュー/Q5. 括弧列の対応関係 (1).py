def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    S = input().rstrip()

    left = []

    # 処理
    ans = 0
    for i, s in enumerate(S):
        if s == "(":
            left.append(i)
        elif s == ")":
            left.pop()
            if len(left) == 0:
                ans = i
                break
    
    # 答えを出力
    print(ans)

if __name__ == '__main__':
    main()