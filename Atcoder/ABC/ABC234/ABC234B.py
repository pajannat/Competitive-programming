def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    zahyo = []
    for i in range(N):
        x, y = map(int, input().split())
        zahyo.append([x, y])
    
    ans = 0
    for xy1 in zahyo:
        x1 = xy1[0]
        y1 = xy1[1]
        for xy2 in zahyo:
            x2 = xy2[0]
            y2 = xy2[1]
            tmp = ((x1-x2)**2 + (y1-y2)**2)**0.5
            ans = max(ans, tmp)

    print(ans)

if __name__ == '__main__':
    main()