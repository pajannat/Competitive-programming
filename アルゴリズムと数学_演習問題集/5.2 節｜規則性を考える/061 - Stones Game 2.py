def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    kaisa = []
    ruiseki = []
    for i in range(61):
        kaisa.append(2**i)
    
    for i, k in enumerate(kaisa):
        if i == 0:
            ruiseki.append(k)
        else:
            hoge = ruiseki[i-1] + k
            ruiseki.append(hoge)
    
    if N in ruiseki:
        print("Second")
    else:
        print("First")


if __name__ == '__main__':
    main()