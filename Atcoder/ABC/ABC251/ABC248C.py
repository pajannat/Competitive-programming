def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())

    # 処理
    chkset = set()
    originpoem = []
    for i in range(N):
        S, T = input().split()
        T = int(T)
        if S not in chkset:
            originpoem.append([i+1, S, T])
        chkset.add(S)
    
    originpoem.sort(key=lambda x: x[2], reverse=True)

    
    # 答えを出力
    print(originpoem[0][0])


if __name__ == '__main__':
    main()