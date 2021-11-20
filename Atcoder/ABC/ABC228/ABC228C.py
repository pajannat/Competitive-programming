def main():
    from sys import stdin
    input = stdin.readline

    N, K = map(int, input().split())

    score = []
    for i in range(N):
        p1, p2, p3 = map(int, input().split())
        score.append([p1+p2+p3, i+1])
    
    score2 = sorted(score, reverse=True)
    border = score2[K-1][0]

    for i in range(N):
        if (border - score[i][0]) <= 300:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()