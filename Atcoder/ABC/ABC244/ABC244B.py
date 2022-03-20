def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    S = input().rstrip()

    houkou = 0
    x = 0
    y = 0
    for s in S:
        if s == "R":
            houkou = (houkou + 1) % 4
        else:
            if houkou == 0:
                x += 1
            elif houkou == 1:
                y -= 1
            elif houkou == 2:
                x -= 1
            else:
                y += 1
    
    print(x, y)

if __name__ == '__main__':
    main()