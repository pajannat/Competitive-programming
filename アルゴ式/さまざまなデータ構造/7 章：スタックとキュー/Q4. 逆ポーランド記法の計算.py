def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    X = input().rstrip()
    N = int(input())
    S = list(input().split())
    num = []
    calc_symbol = ['+', '-', '*', '/']

    # 処理
    for i in range(N):
        if S[i] == '+':
            a = num.pop()
            b = num.pop()
            num.append(b + a)
        elif S[i] == '-':
            a = num.pop()
            b = num.pop()
            num.append(b - a)
        elif S[i] == '*':
            a = num.pop()
            b = num.pop()
            num.append(b * a)
        elif S[i] == '/':
            a = num.pop()
            b = num.pop()
            num.append(b / a)
        else:
            num.append(int(S[i]))
    
    # 答えを出力
    print(X + '=' + str(num[0]))


if __name__ == '__main__':
    main()